#!/usr/bin/env python3
"""
extract_vocal_chart.py
======================
Local Vocal-Chart Extractor Pipeline for Highway Vocal Trainer.

Takes an audio file (.mp3 / .wav) or direct URL (via yt-dlp), isolates the vocal stem using Demucs,
performs forced phonetic word-level alignment using WhisperX, and extracts
fundamental pitch per word and sub-note melismas using librosa.pyin or torchcrepe.

Outputs:
- song_chart.json (Web highway format with sub-note melisma support)
- song.txt (UltraStar / USDX format compatible with Performous / Vocaluxe)
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import webbrowser
from pathlib import Path


def log(msg: str):
    print(f"[extract_vocal_chart] {msg}", flush=True)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Extract word-level timestamps, MIDI pitches, and melismas from song audio."
    )
    parser.add_argument(
        "--audio",
        type=str,
        default=None,
        help="Path to source song audio file (.mp3 or .wav), or direct URL if --url not used.",
    )
    parser.add_argument(
        "--url",
        type=str,
        default=None,
        help="Direct URL (e.g. YouTube, SoundCloud) to download audio via yt-dlp.",
    )
    parser.add_argument(
        "--lyrics",
        type=str,
        default=None,
        help="Optional path to lyrics .txt file. If omitted, WhisperX transcription segments are used.",
    )
    parser.add_argument(
        "--out",
        type=str,
        default="song_chart.json",
        help="Path to output JSON chart file (default: song_chart.json).",
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["json", "ultrastar", "all"],
        default="all",
        help="Export format(s): 'json', 'ultrastar', or 'all' (default: all).",
    )
    parser.add_argument(
        "--pitch-tracker",
        type=str,
        choices=["pyin", "crepe"],
        default="pyin",
        help="Pitch tracking algorithm: 'pyin' (librosa pYIN) or 'crepe' (torchcrepe). Default: pyin.",
    )
    parser.add_argument(
        "--artist",
        type=str,
        default=None,
        help="Optional artist name for metadata and UltraStar headers.",
    )
    parser.add_argument(
        "--demucs-model",
        type=str,
        default="htdemucs",
        help="Demucs model name (default: htdemucs).",
    )
    parser.add_argument(
        "--whisper-model",
        type=str,
        default="medium",
        help="Whisper model name for WhisperX (default: medium).",
    )
    parser.add_argument(
        "--max-duration",
        type=str,
        default=None,
        help="Optional max audio duration to process (e.g. '330' or '5:30'). Trims input if longer.",
    )
    parser.add_argument(
        "--open",
        action="store_true",
        help="Automatically open vocal-highway.html in your default web browser after extraction.",
    )
    return parser.parse_args()


def parse_time_str(time_str: str) -> float:
    """Parse seconds or MM:SS / HH:MM:SS format into float seconds."""
    if not time_str:
        return None
    time_str = str(time_str).strip()
    if ":" in time_str:
        parts = time_str.split(":")
        if len(parts) == 2:
            return float(parts[0]) * 60.0 + float(parts[1])
        elif len(parts) == 3:
            return float(parts[0]) * 3600.0 + float(parts[1]) * 60.0 + float(parts[2])
    return float(time_str)


def download_audio_from_url(url: str, output_dir: Path) -> Path:
    """Download audio from YouTube or any URL supported by yt-dlp."""
    import yt_dlp

    output_dir.mkdir(parents=True, exist_ok=True)
    log(f"Downloading audio from URL: {url} ...")
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": str(output_dir / "%(title)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "quiet": False,
        "no_warnings": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        base, _ = os.path.splitext(filename)
        mp3_path = Path(f"{base}.mp3")
        if not mp3_path.is_file():
            if Path(filename).is_file():
                mp3_path = Path(filename)
        log(f"Downloaded audio to: {mp3_path}")
        return mp3_path


def trim_audio_if_needed(audio_path: Path, max_duration: float) -> Path:
    """Trim audio file to max_duration using ffmpeg if longer."""
    import soundfile as sf

    try:
        info = sf.info(str(audio_path))
        if info.duration <= max_duration + 0.5:
            return audio_path
    except Exception:
        pass

    out_trimmed = Path.cwd() / f"{audio_path.stem}_trimmed_{int(max_duration)}s.mp3"
    if out_trimmed.is_file():
        log(f"Found existing trimmed audio at: {out_trimmed}")
        return out_trimmed

    log(f"Trimming audio to {max_duration:.1f}s via ffmpeg: {out_trimmed.name}...")
    ffmpeg_bin = shutil.which("ffmpeg") or "/opt/homebrew/bin/ffmpeg"
    cmd = [
        ffmpeg_bin,
        "-y",
        "-i",
        str(audio_path),
        "-to",
        str(max_duration),
        "-c",
        "copy",
        str(out_trimmed),
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0 and out_trimmed.is_file():
        return out_trimmed
    else:
        cmd = [
            ffmpeg_bin,
            "-y",
            "-i",
            str(audio_path),
            "-t",
            str(max_duration),
            str(out_trimmed),
        ]
        subprocess.run(cmd, check=True)
        return out_trimmed


def detect_devices():
    """
    Detect optimal computation devices for Demucs, WhisperX, and CREPE.
    Demucs can take advantage of Apple Silicon Metal ('mps') or CUDA.
    WhisperX / faster-whisper on macOS operates reliably on CPU with int8.
    """
    import torch

    has_cuda = torch.cuda.is_available()
    has_mps = hasattr(torch.backends, "mps") and torch.backends.mps.is_available()

    if has_cuda:
        demucs_device = "cuda"
        whisper_device = "cuda"
        compute_type = "float16"
        crepe_device = "cuda"
    elif has_mps:
        demucs_device = "mps"
        whisper_device = "cpu"
        compute_type = "int8"
        crepe_device = "mps"
    else:
        demucs_device = "cpu"
        whisper_device = "cpu"
        compute_type = "int8"
        crepe_device = "cpu"

    log(f"Device config: Demucs={demucs_device}, WhisperX={whisper_device} ({compute_type}), CREPE={crepe_device}")
    return demucs_device, whisper_device, compute_type, crepe_device


def isolate_vocals(audio_path: Path, demucs_device: str, demucs_model: str) -> Path:
    """
    Step 1: Isolate vocals using Demucs if not already cached.
    Checks separated/<demucs_model>/<track_name>/vocals.wav
    """
    track_name = audio_path.stem
    cached_vocals = Path("separated") / demucs_model / track_name / "vocals.wav"

    if cached_vocals.is_file():
        log(f"Found cached vocal stem at: {cached_vocals}")
        return cached_vocals

    log(f"Running Demucs vocal separation for '{audio_path.name}' on {demucs_device}...")

    demucs_bin = shutil.which("demucs")
    if demucs_bin:
        cmd = [
            demucs_bin,
            "--two-stems=vocals",
            "-n",
            demucs_model,
            "-d",
            demucs_device,
            str(audio_path),
        ]
    else:
        cmd = [
            sys.executable,
            "-m",
            "demucs.separate",
            "--two-stems=vocals",
            "-n",
            demucs_model,
            "-d",
            demucs_device,
            str(audio_path),
        ]

    log(f"Executing: {' '.join(cmd)}")
    result = subprocess.run(cmd, check=False)
    if result.returncode != 0:
        if demucs_device == "mps":
            log("Demucs on mps exited with error. Retrying with device='cpu'...")
            cmd[-2] = "cpu"
            subprocess.run(cmd, check=True)
        else:
            raise RuntimeError(f"Demucs failed with exit code {result.returncode}")

    if not cached_vocals.is_file():
        candidates = list(Path("separated").glob(f"*/{track_name}*/vocals.wav"))
        if candidates:
            cached_vocals = candidates[0]
        else:
            raise FileNotFoundError(
                f"Expected vocal stem at {cached_vocals}, but file was not found."
            )

    log(f"Vocal stem generated successfully: {cached_vocals}")
    return cached_vocals


def run_forced_alignment(
    vocals_path: Path,
    whisper_model_name: str,
    whisper_device: str,
    compute_type: str,
):
    """
    Step 2: Transcribe and align word timestamps with WhisperX.
    """
    import whisperx

    log(f"Loading WhisperX audio: {vocals_path}")
    audio = whisperx.load_audio(str(vocals_path))

    log(f"Loading WhisperX model '{whisper_model_name}' on {whisper_device} ({compute_type})...")
    model = whisperx.load_model(
        whisper_model_name,
        device=whisper_device,
        compute_type=compute_type,
        language="en",
    )

    log("Transcribing vocal stem...")
    transcription = model.transcribe(audio, batch_size=16)

    lang_code = transcription.get("language", "en")
    log(f"Loading alignment model for language '{lang_code}'...")
    align_model, metadata = whisperx.load_align_model(
        language_code=lang_code,
        device=whisper_device,
    )

    log("Aligning phonetic word boundaries...")
    aligned_result = whisperx.align(
        transcription["segments"],
        align_model,
        metadata,
        audio,
        whisper_device,
        return_char_alignments=False,
    )

    return aligned_result, audio


def extract_pitch_per_word(
    vocals_path: Path,
    aligned_words: list,
    pitch_tracker: str = "pyin",
    crepe_device: str = "cpu",
) -> list:
    """
    Step 3: Extract fundamental pitch with librosa.pyin or torchcrepe.
    Computes primary median MIDI note and detects melisma (pitch inflections) per word.
    """
    import librosa
    import numpy as np

    fmin = float(librosa.note_to_hz("C2"))  # ~65.4 Hz
    fmax = float(librosa.note_to_hz("C6"))  # ~1046.5 Hz

    if pitch_tracker == "crepe":
        import torch
        import torchcrepe

        log(f"Running neural pitch estimation with torchcrepe on {crepe_device}...")
        y, sr = librosa.load(str(vocals_path), sr=16000)
        hop_length = 160  # 10ms frame resolution
        audio_tensor = torch.tensor(y, dtype=torch.float32).unsqueeze(0)
        
        # Test crepe device compatibility, fallback to cpu if needed
        try:
            pitch, periodicity = torchcrepe.predict(
                audio_tensor,
                sr,
                hop_length=hop_length,
                fmin=fmin,
                fmax=fmax,
                model="tiny",
                batch_size=2048,
                device=crepe_device,
                return_periodicity=True,
            )
        except Exception as e:
            log(f"CREPE device '{crepe_device}' failed ({e}). Retrying on 'cpu'...")
            pitch, periodicity = torchcrepe.predict(
                audio_tensor,
                sr,
                hop_length=hop_length,
                fmin=fmin,
                fmax=fmax,
                model="tiny",
                batch_size=2048,
                device="cpu",
                return_periodicity=True,
            )

        f0 = pitch.squeeze(0).cpu().numpy()
        confidence = periodicity.squeeze(0).cpu().numpy()
        times = np.arange(len(f0)) * (hop_length / sr)
        voiced_mask = (confidence > 0.25) & (f0 > 0)
        f0_midi = np.where(
            voiced_mask,
            69.0 + 12.0 * np.log2(np.maximum(f0, 1e-6) / 440.0),
            np.nan,
        )
    else:
        log(f"Computing pYIN fundamental frequency (sr=22050, C2 ~ C6)...")
        y, sr = librosa.load(str(vocals_path), sr=22050)
        hop_length = 512

        f0, voiced_flag, voiced_probs = librosa.pyin(
            y,
            fmin=fmin,
            fmax=fmax,
            sr=sr,
            hop_length=hop_length,
        )

        if hasattr(librosa, "times_like"):
            times = librosa.times_like(f0, sr=sr, hop_length=hop_length)
        else:
            times = librosa.frames_to_time(np.arange(len(f0)), sr=sr, hop_length=hop_length)

        f0_midi = np.where(
            voiced_flag & (f0 > 0),
            69.0 + 12.0 * np.log2(np.maximum(f0, 1e-6) / 440.0),
            np.nan,
        )

    log("Assigning MIDI pitch and melisma sub-notes to aligned words...")
    last_valid_midi = 60  # Middle C fallback
    results = []

    for w in aligned_words:
        w_text = w["word"].strip()
        w_start = float(w["start"])
        w_end = float(w["end"])
        dur = max(0.05, w_end - w_start)

        # Slice corresponding frames
        mask = (times >= w_start) & (times <= w_end)
        word_frames = f0_midi[mask]
        word_times = times[mask]

        valid_mask = ~np.isnan(word_frames)
        valid_frames = word_frames[valid_mask]
        valid_times = word_times[valid_mask]

        sub_notes = []
        if len(valid_frames) > 0:
            median_midi = int(np.round(np.nanmedian(valid_frames)))
            last_valid_midi = median_midi

            # Melisma detection: detect distinct sustained pitch inflections
            if len(valid_frames) >= 6:
                # 3-frame running median filter to suppress jitter
                smoothed = np.copy(valid_frames)
                for i in range(1, len(valid_frames) - 1):
                    smoothed[i] = np.median(valid_frames[max(0, i - 1) : min(len(valid_frames), i + 2)])

                # Cluster contiguous frames where pitch stays within 1.2 semitones of cluster median
                segments = []
                curr_seg = [0]
                for i in range(1, len(smoothed)):
                    seg_median = np.median(smoothed[curr_seg])
                    if abs(smoothed[i] - seg_median) > 1.2:
                        if len(curr_seg) >= 3:
                            segments.append(curr_seg)
                            curr_seg = [i]
                        else:
                            curr_seg.append(i)
                    else:
                        curr_seg.append(i)
                if curr_seg and len(curr_seg) >= 3:
                    segments.append(curr_seg)

                if len(segments) >= 2:
                    distinct_notes = []
                    for seg in segments:
                        seg_midi = int(np.round(np.median(smoothed[seg])))
                        seg_start = valid_times[seg[0]]
                        seg_end = valid_times[seg[-1]]
                        seg_dur = max(0.05, seg_end - seg_start)
                        distinct_notes.append({
                            "start": float(seg_start),
                            "dur": float(seg_dur),
                            "midi": int(seg_midi),
                        })

                    has_pitch_diff = any(
                        distinct_notes[j]["midi"] != distinct_notes[j - 1]["midi"]
                        for j in range(1, len(distinct_notes))
                    )

                    if has_pitch_diff:
                        # Scale sub-notes proportionally to span the full word duration seamlessly
                        total_seg_dur = sum(n["dur"] for n in distinct_notes)
                        if total_seg_dur > 0:
                            cur_t = round(w_start, 3)
                            for n in distinct_notes:
                                prop_dur = max(0.05, (n["dur"] / total_seg_dur) * dur)
                                sub_notes.append({
                                    "start": round(cur_t, 3),
                                    "dur": round(prop_dur, 3),
                                    "midi": n["midi"],
                                })
                                cur_t += prop_dur
        else:
            median_midi = last_valid_midi

        word_dict = {
            "text": w_text,
            "start": round(w_start, 3),
            "dur": round(dur, 3),
            "midi": int(median_midi),
        }
        if sub_notes:
            word_dict["subNotes"] = sub_notes

        results.append(word_dict)

    return results


def map_words_to_lyrics(all_words: list, lyrics_file: Path) -> list:
    """
    Map the flattened list of aligned words onto user-provided lyrics lines.
    Preserves verse/chorus section titles if headers like [Verse 1] are present.
    """
    log(f"Mapping words onto user line breaks from: {lyrics_file}")
    with open(lyrics_file, "r", encoding="utf-8") as f:
        raw_lines = [line.strip() for line in f.readlines()]

    current_section = "Line 1"
    user_lines = []
    for raw in raw_lines:
        if not raw:
            continue
        if raw.startswith("[") and raw.endswith("]"):
            current_section = raw[1:-1].strip()
            continue
        user_lines.append((current_section, raw))

    if not user_lines:
        log("No valid lyrics lines found in file. Using raw segments.")
        return None

    word_idx = 0
    total_words = len(all_words)
    chart_lines = []

    for sec_name, user_text in user_lines:
        tokens = user_text.split()
        if not tokens:
            continue

        line_words = []
        for token in tokens:
            if word_idx < total_words:
                w_data = dict(all_words[word_idx])
                w_data["text"] = token
                line_words.append(w_data)
                word_idx += 1
            else:
                last_start = line_words[-1]["start"] + line_words[-1]["dur"] if line_words else 0.0
                last_midi = line_words[-1]["midi"] if line_words else 60
                line_words.append({
                    "text": token,
                    "start": round(last_start + 0.05, 3),
                    "dur": 0.35,
                    "midi": last_midi,
                })

        if line_words:
            chart_lines.append({
                "section": sec_name,
                "fullLine": user_text,
                "startTime": line_words[0]["start"],
                "words": line_words,
            })

    return chart_lines


def build_chart_from_segments(segments: list, words_with_pitch: list) -> list:
    """
    Construct chart lines from aligned words, grouping them into natural
    musical phrases based on pauses and punctuation for clean teleprompter display.
    """
    if not words_with_pitch:
        return []

    phrases = []
    curr_phrase = []

    for w in words_with_pitch:
        if not curr_phrase:
            curr_phrase.append(w)
            continue

        prev_w = curr_phrase[-1]
        prev_end = prev_w["start"] + prev_w["dur"]
        gap = w["start"] - prev_end
        has_punct = bool(re.search(r"[,.?!;:]$", prev_w["text"]))

        # Split on natural musical pauses
        if gap >= 0.9 or (gap >= 0.5 and has_punct) or (gap >= 0.6 and len(curr_phrase) >= 6):
            phrases.append(curr_phrase)
            curr_phrase = [w]
        else:
            curr_phrase.append(w)

    if curr_phrase:
        phrases.append(curr_phrase)

    chart_lines = []
    for idx, p in enumerate(phrases):
        line_text = " ".join(w["text"] for w in p)
        chart_lines.append({
            "section": f"Phrase {idx + 1}",
            "fullLine": line_text,
            "startTime": p[0]["start"],
            "words": p,
        })

    return chart_lines


def export_ultrastar_format(
    chart_payload: dict,
    out_txt_path: Path,
    audio_filename: str = None,
    bpm: float = 120.0,
    artist: str = "Unknown Artist",
) -> Path:
    """
    Export song chart to standard UltraStar format (.txt).
    BPM in UltraStar uses 4 beats per quarter note (16th notes).
    Pitch 0 is typically C4 (MIDI note 60).
    """
    title = chart_payload.get("title", "Song")
    lines = chart_payload.get("lines", [])

    out_lines = [
        f"#TITLE:{title}",
        f"#ARTIST:{artist}",
    ]
    if audio_filename:
        out_lines.append(f"#MP3:{audio_filename}")

    # Beat duration in seconds: 60 / (bpm * 4)
    beat_dur = 60.0 / (bpm * 4.0)
    gap_ms = 0
    if lines and lines[0].get("words"):
        first_start = lines[0]["words"][0]["start"]
        gap_ms = int(max(0, first_start * 1000.0))

    out_lines.append(f"#BPM:{bpm:.2f}")
    out_lines.append(f"#GAP:{gap_ms}")

    gap_sec = gap_ms / 1000.0
    last_line_end_beat = 0

    for l_idx, line in enumerate(lines):
        words = line.get("words", [])
        if not words:
            continue

        for w_idx, w in enumerate(words):
            sub_notes = w.get("subNotes", [])
            w_text = w.get("text", "")

            if sub_notes and len(sub_notes) > 1:
                for s_idx, sn in enumerate(sub_notes):
                    rel_start = max(0.0, sn["start"] - gap_sec)
                    start_beat = int(round(rel_start / beat_dur))
                    dur_beats = max(1, int(round(sn["dur"] / beat_dur)))
                    us_pitch = sn["midi"] - 60
                    trail = " " if (s_idx == len(sub_notes) - 1) else "~"
                    syl = (w_text if s_idx == 0 else "~") + trail
                    out_lines.append(f": {start_beat} {dur_beats} {us_pitch} {syl}")
                    last_line_end_beat = start_beat + dur_beats
            else:
                rel_start = max(0.0, w["start"] - gap_sec)
                start_beat = int(round(rel_start / beat_dur))
                dur_beats = max(1, int(round(w["dur"] / beat_dur)))
                us_pitch = w.get("midi", 60) - 60
                out_lines.append(f": {start_beat} {dur_beats} {us_pitch} {w_text} ")
                last_line_end_beat = start_beat + dur_beats

        if l_idx < len(lines) - 1:
            next_start_beat = last_line_end_beat + 4
            out_lines.append(f"- {next_start_beat}")

    out_lines.append("E")

    out_txt_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_txt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(out_lines) + "\n")

    log(f"UltraStar chart exported -> {out_txt_path}")
    return out_txt_path


def main():
    args = parse_args()

    # Handle input audio vs URL
    audio_input = args.audio
    if args.url:
        audio_input = args.url
    elif not audio_input:
        log("Error: Please provide --audio <file> or --url <web_link>.")
        sys.exit(1)

    # Check if audio_input is a URL
    if str(audio_input).startswith("http://") or str(audio_input).startswith("https://"):
        downloads_dir = Path.cwd() / "audio_downloads"
        audio_path = download_audio_from_url(str(audio_input), downloads_dir)
    else:
        audio_path = Path(audio_input).resolve()
        if not audio_path.is_file():
            log(f"Error: audio file not found: {audio_path}")
            sys.exit(1)

    lyrics_path = Path(args.lyrics).resolve() if args.lyrics else None
    if lyrics_path and not lyrics_path.is_file():
        log(f"Warning: lyrics file not found at {lyrics_path}. Proceeding without it.")
        lyrics_path = None

    out_path = Path(args.out).resolve()
    max_duration = parse_time_str(args.max_duration) if args.max_duration else None

    # Trim audio file if requested
    if max_duration is not None:
        log(f"Trimming audio to maximum duration {max_duration:.2f}s...")
        audio_to_process = trim_audio_if_needed(audio_path, max_duration)
    else:
        audio_to_process = audio_path

    demucs_dev, whisper_dev, compute_type, crepe_dev = detect_devices()

    # 1. Vocal Isolation
    vocals_wav = isolate_vocals(audio_to_process, demucs_dev, args.demucs_model)

    # 2. Forced Alignment with WhisperX
    alignment_result, audio_data = run_forced_alignment(
        vocals_wav,
        args.whisper_model,
        whisper_dev,
        compute_type,
    )

    # Flatten and validate aligned words
    raw_segments = alignment_result.get("segments", [])
    flat_words = []
    current_time = 0.0

    for seg in raw_segments:
        seg_start = seg.get("start", current_time)
        seg_words = seg.get("words", [])

        for w in seg_words:
            w_text = w.get("word", "").strip()
            if not w_text:
                continue
            w_start = w.get("start")
            w_end = w.get("end")
            if w_start is None:
                w_start = current_time
            if w_end is None:
                w_end = w_start + 0.3

            flat_words.append({
                "word": w_text,
                "start": float(w_start),
                "end": float(w_end),
            })
            current_time = float(w_end)

    if max_duration is not None:
        flat_words = [w for w in flat_words if w["start"] < max_duration]
        for w in flat_words:
            if w["end"] > max_duration:
                w["end"] = max_duration

    if not flat_words:
        log("No words detected by WhisperX. Creating fallback single-word entry.")
        flat_words.append({"word": "Vocals", "start": 0.0, "end": min(2.0, max_duration or 2.0)})

    # 3. Pitch Extraction via librosa.pyin or torchcrepe
    words_with_pitch = extract_pitch_per_word(
        vocals_wav,
        flat_words,
        pitch_tracker=args.pitch_tracker,
        crepe_device=crepe_dev,
    )

    # 4. Line Grouping (User lyrics or WhisperX segments)
    if lyrics_path:
        lines = map_words_to_lyrics(words_with_pitch, lyrics_path)
        if not lines:
            lines = build_chart_from_segments(raw_segments, words_with_pitch)
    else:
        lines = build_chart_from_segments(raw_segments, words_with_pitch)

    # Calculate song duration
    import soundfile as sf

    try:
        info = sf.info(str(vocals_wav))
        duration = round(float(info.duration), 2)
    except Exception:
        duration = round(float(len(audio_data) / 16000.0), 2)

    if max_duration is not None:
        duration = min(duration, round(float(max_duration), 2))

    # Song title cleaned from audio filename
    raw_title = audio_path.stem
    if "_trimmed_" in raw_title:
        raw_title = raw_title.split("_trimmed_")[0]
    title = raw_title.replace("_", " ").replace("-", " ").title()
    artist_name = args.artist or "Artist"

    chart_payload = {
        "title": title,
        "artist": artist_name,
        "duration": duration,
        "lines": lines,
    }

    # Export formats
    if args.format in ["json", "all"]:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(chart_payload, f, indent=2, ensure_ascii=False)
        log(f"Successfully generated song chart with {len(lines)} lines -> {out_path}")

    if args.format in ["ultrastar", "all"]:
        txt_out_path = out_path.with_suffix(".txt")
        export_ultrastar_format(
            chart_payload,
            txt_out_path,
            audio_filename=audio_path.name,
            artist=artist_name,
        )

    # Open in browser if requested
    if args.open:
        html_file = Path("vocal-highway.html").resolve()
        if html_file.is_file():
            log(f"Opening browser at: file://{html_file}")
            webbrowser.open(f"file://{html_file}")
        else:
            log("vocal-highway.html not found to open automatically.")


if __name__ == "__main__":
    main()
