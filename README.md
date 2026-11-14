# 🎤 Vocal Highway

> **Local AI Vocal Chart Extractor & Interactive Browser Highway Trainer**  
> Isolate vocals with Demucs, perform word-level phonetic alignment with WhisperX, extract continuous pitch & melisma inflections with pYIN / CREPE, and train your voice on a zero-dependency HTML5 Canvas highway player with real-time mic tracking.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Apple Silicon Metal](https://img.shields.io/badge/Accelerated-Apple%20Metal%20MPS-purple.svg)](https://developer.apple.com/metal/)
[![Web Audio API](https://img.shields.io/badge/Player-Zero%20Dependency%20HTML5-orange.svg)](vocal-highway.html)

---

## 🌟 Overview & Architecture

Vocal Highway bridges the gap between state-of-the-art local AI audio models and real-time browser game technology. It allows singers, vocal coaches, and music hobbyists to take any song file (or YouTube link), isolate the vocal track, extract exact word timestamps and musical pitches (including runs and ornaments), and sing along with real-time pitch intonation feedback.

```
                                  [ Song Audio (.mp3/.wav) or YouTube URL ]
                                                      │
                                                      ▼
                                       ┌─────────────────────────────┐
                                       │     Demucs (htdemucs)       │  Metal MPS / CUDA
                                       │     Vocal Stem Isolation    │
                                       └──────────────┬──────────────┘
                                                      │ vocals.wav
                                                      ▼
                                       ┌─────────────────────────────┐
                                       │          WhisperX           │  Forced Phonetic
                                       │    Word-Level Alignment     │  Timestamping
                                       └──────────────┬──────────────┘
                                                      │ [start, end]
                                                      ▼
                                       ┌─────────────────────────────┐
                                       │   librosa.pyin / CREPE      │  Pitch Extraction &
                                       │     Melisma Clustering      │  Melisma Sub-Notes
                                       └──────────────┬──────────────┘
                                                      │
                                       ┌──────────────┴──────────────┐
                                       ▼                             ▼
                          ┌───────────────────────────┐ ┌───────────────────────────┐
                          │     song_chart.json       │ │         song.txt          │
                          │   (Web Highway Format)    │ │    (UltraStar / USDX)     │
                          └─────────────┬─────────────┘ └───────────────────────────┘
                                        │
                                        ▼
                   ┌───────────────────────────────────────────────┐
                   │               vocal-highway.html              │
                   │  - HTML5 Canvas Vocal Highway                 │
                   │  - Real-time Mic Autocorrelation Pitch Track  │
                   │  - Continuous Neon Pitch Ribbon (Smule-style) │
                   │  - Intonation Cents Meter Badge (±Cents)      │
                   │  - Dual-Stem Audio Balance (Vocals/Backing)   │
                   │  - A-B Practice Looper                        │
                   │  - Vocal Range Profile & Auto-Key Shift       │
                   │  - End-of-Song Scorecard & Analytics Modal    │
                   │  - Built-in Vocal Warm-Up Exercises           │
                   └───────────────────────────────────────────────┘
```

---

## ✨ Key Features

### 1. Browser Vocal Highway Player (`vocal-highway.html`)
- **Zero-Dependency Single File:** Pure HTML5 Canvas, Web Audio API, and vanilla JavaScript. Opens directly from your local disk (`file://`) without CORS issues, node servers, or external CDNs.
- **Continuous Sung Pitch Ribbon (Smule / SingStar Style):** Visualizes your live vocal intonation, vibrato, and pitch glides as a glowing neon ribbon trailing behind the playhead.
- **Real-Time Intonation Cents Meter:** Displays an exact floating pill badge at your voice cursor (`+15¢ Sharp`, `0¢ In Tune`, `-20¢ Flat`) for immediate tuning feedback.
- **Dual-Stem Audio Balance:** Load both `vocals.wav` and `no_vocals.wav` (or backing audio) with a live crossfader slider to transition smoothly from learning with the guide singer to singing solo karaoke.
- **A-B Practice Looper:** Press `[A] Set Start` and `[B] Set End` to loop any challenging 5-second vocal run seamlessly until you master it.
- **Vocal Range Profile & Smart Key Transposition:** Profiles your comfortable sung range (min/max MIDI) against the song's tessitura, with one-click `[✨ Auto-Fit Range]` transposition (-6 to +2 semitones).
- **End-of-Song Scorecard Modal:** Summary of your overall hit accuracy, sharp/flat intonation bias, and phrase-by-phrase rating with a `[🔁 Practice Hardest Phrase]` jump button.
- **Built-in Vocal Warm-Up Charts:** Includes pre-packaged warm-ups: 5-Tone Scale, Octave Arpeggio, and Vocal Sirens (Glissando).
- **Phase-Locked Loop (PLL) Time Sync:** Smooth audio clock synchronization eliminates hardware buffer jitter and ensures buttery 60/120 FPS scrolling.

### 2. Audio Extraction Pipeline (`extract_vocal_chart.py`)
- **Demucs Stem Separation:** Isolates vocal stems locally using `htdemucs`, accelerated by Apple Silicon Metal (`mps`) or NVIDIA CUDA.
- **WhisperX Forced Alignment:** Transcribes and aligns phonemes to sub-millisecond accuracy.
- **Melisma & Syllable Run Extraction:** Detects pitch inflection plateaus within single words, generating `subNotes` for vocal runs and ornamentation.
- **DSP or Neural Pitch Trackers:** Supports fast, accurate `librosa.pyin` or neural `torchcrepe` (`--pitch-tracker pyin|crepe`).
- **YouTube / URL Ingestion:** Directly pass any online audio or YouTube video URL via `--url` with automatic `yt-dlp` download.
- **UltraStar / USDX Exporter:** Generates standard UltraStar `.txt` files compatible with Performous, Vocaluxe, and UltraStar Deluxe.
- **Auto-Launch:** Pass `--open` to immediately launch `vocal-highway.html` in your default browser once extraction finishes.

---

## 🚀 Quick Start

### 1. Clone & Set Up Environment

```bash
git clone https://github.com/ejde/vocal-highway.git
cd vocal-highway

# Create Python virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

*(Ensure `ffmpeg` is installed on your system: `brew install ffmpeg` on macOS or `sudo apt install ffmpeg` on Linux).*

### 2. Run the Web Highway Trainer (Immediate Play)

Double-click `vocal-highway.html` in your file explorer or open it in your browser:
```bash
open vocal-highway.html
```
- Click **🎤 Enable Mic** and allow microphone access.
- Click **▶ Start** to practice with the embedded vocal chart.
- Select **Warm-Up: 5-Tone Scale** from the preset dropdown to warm up your voice first!

### 3. Extract a Song Chart from Audio or YouTube

```bash
# From a local audio file (.mp3 / .wav)
python extract_vocal_chart.py --audio "path/to/song.mp3" --open

# From a YouTube URL
python extract_vocal_chart.py --url "https://www.youtube.com/watch?v=..." --open

# Process first 5 minutes and 30 seconds with neural CREPE pitch tracking:
python extract_vocal_chart.py --audio song.mp3 --max-duration 5:30 --pitch-tracker crepe --open
```

The script organizes each extracted song into `charts/<song-slug>/`:
- `charts/<song-slug>/<song-slug>.json` — Structured highway chart with melisma sub-notes
- `charts/<song-slug>/<song-slug>.txt` — Standard UltraStar format chart
- `charts/<song-slug>/vocals.wav` — Clean isolated vocal guide stem
- `charts/<song-slug>/no_vocals.wav` — Instrumental backing stem

---

## 🛠️ CLI Reference (`extract_vocal_chart.py`)

| Argument | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `--audio` | `str` | `None` | Path to local song audio file (`.mp3` or `.wav`). |
| `--url` | `str` | `None` | Online URL (e.g. YouTube) to download via `yt-dlp`. |
| `--lyrics` | `str` | `None` | Optional lyrics `.txt` file to format line breaks and phrases. |
| `--out` | `str` | `charts/<slug>/<slug>.json` | Optional custom path for exported JSON song chart. |
| `--format` | `str` | `all` | Export formats: `json`, `ultrastar`, or `all`. |
| `--pitch-tracker` | `str` | `pyin` | Pitch algorithm: `pyin` (pYIN) or `crepe` (torchcrepe). |
| `--artist` | `str` | `None` | Artist name for metadata and UltraStar headers. |
| `--max-duration` | `str` | `None` | Max duration to process (e.g. `330` or `5:30`). |
| `--demucs-model` | `str` | `htdemucs` | Demucs model name. |
| `--whisper-model`| `str` | `medium` | Whisper model for WhisperX alignment. |
| `--open` | `flag` | `False` | Auto-launch `vocal-highway.html` upon completion. |

---

## 📋 JSON Chart Schema (`song_chart.json`)

```json
{
  "title": "Song Title",
  "artist": "Artist Name",
  "duration": 222.5,
  "lines": [
    {
      "section": "Phrase 1",
      "fullLine": "Amazing grace how sweet the sound",
      "startTime": 2.0,
      "words": [
        { "text": "Amazing", "start": 2.0, "dur": 0.95, "midi": 65 },
        { "text": "grace,", "start": 4.0, "dur": 1.20, "midi": 65 },
        { "text": "how", "start": 5.4, "dur": 0.45, "midi": 69 },
        {
          "text": "sweet",
          "start": 5.9,
          "dur": 0.90,
          "midi": 67,
          "subNotes": [
            { "start": 5.9, "dur": 0.45, "midi": 67 },
            { "start": 6.35, "dur": 0.45, "midi": 69 }
          ]
        }
      ]
    }
  ]
}
```

---

## ⌨️ Browser Controls & Keyboard Shortcuts

- `Space`: Play / Pause toggle
- `Scrubber Slider`: Seek anywhere instantly across the song
- `[A] / [B] / ❌`: Set and clear A-B practice loop points
- `Key [-] / [+]`: Transpose song by semitones (-6 to +2)
- `✨ Auto-Fit Range`: Automatically transposes the chart to center on your comfortable voice register
- `🎸 Backing [─────🔘─────] 🎙️ Vocals`: Crossfade between instrumental karaoke and vocal guide
- `🏎️ Scroll Speed`: Toggle highway velocity (180, 280, 380, 480 px/s)
- `Sync [-50ms] / [+50ms]`: Adjust audio-to-visual latency calibration

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
Feel free to use, modify, and distribute it for personal practice, music education, and karaoke software!
