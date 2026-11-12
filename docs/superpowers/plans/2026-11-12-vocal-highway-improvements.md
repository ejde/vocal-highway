# Vocal Highway Full Feature Suite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform the Vocal Highway project into a feature-complete, open-source-ready vocal practice ecosystem with melisma detection, neural pitch tracking, YouTube ingestion, UltraStar export, continuous singing pitch ribbon, dual-stem audio mixing, A-B practice looper, vocal range analytics, and complete repository packaging.

**Architecture:** 
1. Upgrade `extract_vocal_chart.py` with multi-note melisma segmentation, optional CREPE neural pitch tracking, UltraStar `.txt` exporter, `yt-dlp` download, and `--open` auto-launch.
2. Upgrade `vocal-highway.html` with continuous sung pitch ribbon visualizer, sharp/flat intonation meter, dual-stem audio crossfader, A-B section looper, vocal range analyzer, end-of-song scorecard modal, and built-in vocal warm-up charts.
3. Add open-source repository assets: `LICENSE`, `.gitignore`, `requirements.txt`, procedural demo audio/chart, and comprehensive `README.md`.

**Tech Stack:** Python 3.11+, PyTorch (MPS / CUDA / CPU), Demucs, WhisperX, Librosa, Torchcrepe, yt-dlp, HTML5 Canvas, Web Audio API, Vanilla JavaScript.

## Global Constraints
- Pure zero-dependency browser runtime for `vocal-highway.html` (runs directly via `file://`).
- No breaking changes to existing `song_chart.json` schema (backward-compatible).
- Python scripts must support Apple Silicon Metal (`mps`) and graceful CPU fallback.

---

### Task 1: Pipeline Melisma & Multi-Note Syllable Extraction

**Files:**
- Modify: `extract_vocal_chart.py`
- Test: `test_pipeline.py`

**Interfaces:**
- Consumes: Aligned word boundaries `[start, end]` and frame-level f0 pitches.
- Produces: Word structures where words with pitch runs contain sub-notes (`sub_notes: [{"start": t, "dur": d, "midi": m}]`) and split visual bars.

- [ ] **Step 1: Write unit test for melisma splitting**
- [ ] **Step 2: Implement frame-level pitch inflection segmentation in `extract_pitch_per_word`**
- [ ] **Step 3: Run unit test to verify melisma segments are produced**

---

### Task 2: UltraStar `.txt` Exporter & CLI Additions (`yt-dlp`, `--open`, `--format`)

**Files:**
- Modify: `extract_vocal_chart.py`
- Test: `test_ultrastar_export.py`

**Interfaces:**
- Consumes: Aligned and pitched song chart data.
- Produces: Standard UltraStar format `.txt` file (`#TITLE`, `#BPM`, `#GAP`, `: <start> <length> <pitch> <word>`) and optional URL downloader via `yt-dlp`.

- [ ] **Step 1: Implement UltraStar exporter function `export_ultrastar_format`**
- [ ] **Step 2: Add `--format json,ultrastar`, `--url`, and `--open` flags to CLI argument parser**
- [ ] **Step 3: Test export on existing chart and verify UltraStar syntax**

---

### Task 3: Continuous Sung Pitch Ribbon & Intonation Cents Meter

**Files:**
- Modify: `vocal-highway.html`

**Interfaces:**
- Consumes: Real-time detected MIDI notes from `detectPitch()`.
- Produces: Continuous scrolling canvas pitch trail (ribbon) and real-time intonation gauge (`+14¢ Sharp`, `0¢ In Tune`, `-18¢ Flat`).

- [ ] **Step 1: Add rolling pitch history buffer `pitchHistory` in JS**
- [ ] **Step 2: Render smooth neon curved ribbon trailing backwards from playhead**
- [ ] **Step 3: Add sharp/flat deviation badge at the cursor**
- [ ] **Step 4: Verify rendering and performance in browser**

---

### Task 4: Dual-Stem Audio Balance & A-B Practice Looper

**Files:**
- Modify: `vocal-highway.html`

**Interfaces:**
- Consumes: Two HTMLAudioElements or Web Audio buffer nodes (`vocals` and `no_vocals`).
- Produces: Real-time guide-vocal-to-backing crossfade and loop boundary enforcement.

- [ ] **Step 1: Add dual audio loader in header (Vocals stem + Backing stem)**
- [ ] **Step 2: Implement synchronized play/pause/seek and crossfade gain slider**
- [ ] **Step 3: Implement `[Set A]`, `[Set B]`, `[Clear Loop]` transport controls**
- [ ] **Step 4: Verify seamless looping and crossfading**

---

### Task 5: Vocal Range Profile, Scorecard Modal & Warm-Up Charts

**Files:**
- Modify: `vocal-highway.html`

**Interfaces:**
- Consumes: Session pitch performance frames and chart pitch limits.
- Produces: Vocal range comparison, post-performance analytics modal, and 3 built-in vocal warm-up exercises.

- [ ] **Step 1: Add procedural vocal warm-up charts (5-tone scale, octave siren, arpeggio)**
- [ ] **Step 2: Implement post-song summary modal with accuracy %, flat/sharp bias, and section ratings**
- [ ] **Step 3: Add vocal range detector showing singer's range vs song range**

---

### Task 6: Open-Source Packaging & Documentation

**Files:**
- Create: `LICENSE` (MIT)
- Create: `requirements.txt`
- Create: `.gitignore`
- Create: `README.md`
- Create: `demo_chart.json` (royalty-free starter chart)

**Interfaces:**
- Consumes: Complete project directory.
- Produces: Production-ready GitHub repository with documentation, badges, and quick start guide.

- [ ] **Step 1: Create `LICENSE` (MIT License)**
- [ ] **Step 2: Create `requirements.txt` with dependencies**
- [ ] **Step 3: Create `.gitignore` to prevent committing audio stems and caches**
- [ ] **Step 4: Write comprehensive `README.md` with visual guide and architecture diagram**
- [ ] **Step 5: Verify all deliverables**
