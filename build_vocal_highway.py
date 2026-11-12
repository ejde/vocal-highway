import json
from pathlib import Path

# Load public-domain demo_chart.json
with open("demo_chart.json", "r", encoding="utf-8") as f:
    demo_chart_json_str = f.read()

# Generate warm-up charts
warmup_5tone = {
    "title": "Warm-Up: 5-Tone Scale",
    "artist": "Vocal Highway Coach",
    "duration": 45.0,
    "lines": [
        {
            "section": "Pattern 1 (C Major)",
            "fullLine": "Do Re Mi Fa Sol Fa Mi Re Do",
            "startTime": 2.0,
            "words": [
                {"text": "Do", "start": 2.0, "dur": 0.45, "midi": 60},
                {"text": "Re", "start": 2.5, "dur": 0.45, "midi": 62},
                {"text": "Mi", "start": 3.0, "dur": 0.45, "midi": 64},
                {"text": "Fa", "start": 3.5, "dur": 0.45, "midi": 65},
                {"text": "Sol", "start": 4.0, "dur": 0.70, "midi": 67},
                {"text": "Fa", "start": 4.8, "dur": 0.45, "midi": 65},
                {"text": "Mi", "start": 5.3, "dur": 0.45, "midi": 64},
                {"text": "Re", "start": 5.8, "dur": 0.45, "midi": 62},
                {"text": "Do", "start": 6.3, "dur": 0.90, "midi": 60},
            ]
        },
        {
            "section": "Pattern 2 (D Major)",
            "fullLine": "Do Re Mi Fa Sol Fa Mi Re Do",
            "startTime": 9.0,
            "words": [
                {"text": "Do", "start": 9.0, "dur": 0.45, "midi": 62},
                {"text": "Re", "start": 9.5, "dur": 0.45, "midi": 64},
                {"text": "Mi", "start": 10.0, "dur": 0.45, "midi": 66},
                {"text": "Fa", "start": 10.5, "dur": 0.45, "midi": 67},
                {"text": "Sol", "start": 11.0, "dur": 0.70, "midi": 69},
                {"text": "Fa", "start": 11.8, "dur": 0.45, "midi": 67},
                {"text": "Mi", "start": 12.3, "dur": 0.45, "midi": 66},
                {"text": "Re", "start": 12.8, "dur": 0.45, "midi": 64},
                {"text": "Do", "start": 13.3, "dur": 0.90, "midi": 62},
            ]
        },
        {
            "section": "Pattern 3 (E Major)",
            "fullLine": "Do Re Mi Fa Sol Fa Mi Re Do",
            "startTime": 16.0,
            "words": [
                {"text": "Do", "start": 16.0, "dur": 0.45, "midi": 64},
                {"text": "Re", "start": 16.5, "dur": 0.45, "midi": 66},
                {"text": "Mi", "start": 17.0, "dur": 0.45, "midi": 68},
                {"text": "Fa", "start": 17.5, "dur": 0.45, "midi": 69},
                {"text": "Sol", "start": 18.0, "dur": 0.70, "midi": 71},
                {"text": "Fa", "start": 18.8, "dur": 0.45, "midi": 69},
                {"text": "Mi", "start": 19.3, "dur": 0.45, "midi": 68},
                {"text": "Re", "start": 19.8, "dur": 0.45, "midi": 66},
                {"text": "Do", "start": 20.3, "dur": 0.90, "midi": 64},
            ]
        },
        {
            "section": "Pattern 4 (F Major)",
            "fullLine": "Do Re Mi Fa Sol Fa Mi Re Do",
            "startTime": 23.0,
            "words": [
                {"text": "Do", "start": 23.0, "dur": 0.45, "midi": 65},
                {"text": "Re", "start": 23.5, "dur": 0.45, "midi": 67},
                {"text": "Mi", "start": 24.0, "dur": 0.45, "midi": 69},
                {"text": "Fa", "start": 24.5, "dur": 0.45, "midi": 70},
                {"text": "Sol", "start": 25.0, "dur": 0.70, "midi": 72},
                {"text": "Fa", "start": 25.8, "dur": 0.45, "midi": 70},
                {"text": "Mi", "start": 26.3, "dur": 0.45, "midi": 69},
                {"text": "Re", "start": 26.8, "dur": 0.45, "midi": 67},
                {"text": "Do", "start": 27.3, "dur": 0.90, "midi": 65},
            ]
        }
    ]
}

warmup_arpeggio = {
    "title": "Warm-Up: Octave Arpeggio",
    "artist": "Vocal Highway Coach",
    "duration": 40.0,
    "lines": [
        {
            "section": "Arpeggio 1 (C Major)",
            "fullLine": "Ah Ah Ah Ah Ah Ah Ah",
            "startTime": 2.0,
            "words": [
                {"text": "Ah (1)", "start": 2.0, "dur": 0.5, "midi": 60},
                {"text": "Ah (3)", "start": 2.6, "dur": 0.5, "midi": 64},
                {"text": "Ah (5)", "start": 3.2, "dur": 0.5, "midi": 67},
                {"text": "Ah (8)", "start": 3.8, "dur": 0.8, "midi": 72},
                {"text": "Ah (5)", "start": 4.7, "dur": 0.5, "midi": 67},
                {"text": "Ah (3)", "start": 5.3, "dur": 0.5, "midi": 64},
                {"text": "Ah (1)", "start": 5.9, "dur": 0.9, "midi": 60},
            ]
        },
        {
            "section": "Arpeggio 2 (D Major)",
            "fullLine": "Ah Ah Ah Ah Ah Ah Ah",
            "startTime": 8.5,
            "words": [
                {"text": "Ah (1)", "start": 8.5, "dur": 0.5, "midi": 62},
                {"text": "Ah (3)", "start": 9.1, "dur": 0.5, "midi": 66},
                {"text": "Ah (5)", "start": 9.7, "dur": 0.5, "midi": 69},
                {"text": "Ah (8)", "start": 10.3, "dur": 0.8, "midi": 74},
                {"text": "Ah (5)", "start": 11.2, "dur": 0.5, "midi": 69},
                {"text": "Ah (3)", "start": 11.8, "dur": 0.5, "midi": 66},
                {"text": "Ah (1)", "start": 12.4, "dur": 0.9, "midi": 62},
            ]
        },
        {
            "section": "Arpeggio 3 (E Major)",
            "fullLine": "Ah Ah Ah Ah Ah Ah Ah",
            "startTime": 15.0,
            "words": [
                {"text": "Ah (1)", "start": 15.0, "dur": 0.5, "midi": 64},
                {"text": "Ah (3)", "start": 15.6, "dur": 0.5, "midi": 68},
                {"text": "Ah (5)", "start": 16.2, "dur": 0.5, "midi": 71},
                {"text": "Ah (8)", "start": 16.8, "dur": 0.8, "midi": 76},
                {"text": "Ah (5)", "start": 17.7, "dur": 0.5, "midi": 71},
                {"text": "Ah (3)", "start": 18.3, "dur": 0.5, "midi": 68},
                {"text": "Ah (1)", "start": 18.9, "dur": 0.9, "midi": 64},
            ]
        }
    ]
}

warmup_siren = {
    "title": "Warm-Up: Vocal Sirens (Glissando)",
    "artist": "Vocal Highway Coach",
    "duration": 36.0,
    "lines": [
        {
            "section": "Siren 1 (Low to Mid)",
            "fullLine": "Whoo-oo-oo-ooh",
            "startTime": 2.0,
            "words": [
                {
                    "text": "Whoo-oo-oo-ooh",
                    "start": 2.0,
                    "dur": 4.5,
                    "midi": 55,
                    "subNotes": [
                        {"start": 2.0, "dur": 0.75, "midi": 50},
                        {"start": 2.75, "dur": 0.75, "midi": 54},
                        {"start": 3.5, "dur": 0.75, "midi": 58},
                        {"start": 4.25, "dur": 0.75, "midi": 62},
                        {"start": 5.0, "dur": 0.75, "midi": 58},
                        {"start": 5.75, "dur": 0.75, "midi": 52},
                    ]
                }
            ]
        },
        {
            "section": "Siren 2 (Full Range Chest to Head)",
            "fullLine": "Whoo-oo-oo-ooh",
            "startTime": 8.0,
            "words": [
                {
                    "text": "Whoo-oo-oo-ooh",
                    "start": 8.0,
                    "dur": 6.0,
                    "midi": 62,
                    "subNotes": [
                        {"start": 8.0, "dur": 0.75, "midi": 52},
                        {"start": 8.75, "dur": 0.75, "midi": 57},
                        {"start": 9.5, "dur": 0.75, "midi": 62},
                        {"start": 10.25, "dur": 0.75, "midi": 67},
                        {"start": 11.0, "dur": 0.75, "midi": 72},
                        {"start": 11.75, "dur": 0.75, "midi": 67},
                        {"start": 12.5, "dur": 0.75, "midi": 60},
                        {"start": 13.25, "dur": 0.75, "midi": 52},
                    ]
                }
            ]
        }
    ]
}

warmup_json = {
    "warmup_5tone": warmup_5tone,
    "warmup_arpeggio": warmup_arpeggio,
    "warmup_siren": warmup_siren
}

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vocal Highway — Interactive Pitch Trainer & Karaoke Studio</title>
  <style>
    :root {{
      --bg-dark: #0a0d14;
      --bg-card: #121824;
      --bg-card-hover: #182234;
      --border-color: #222f46;
      --accent-cyan: #06b6d4;
      --accent-cyan-glow: rgba(6, 182, 212, 0.45);
      --accent-green: #22c55e;
      --accent-green-glow: rgba(34, 197, 94, 0.6);
      --accent-purple: #8b5cf6;
      --accent-amber: #f59e0b;
      --accent-rose: #f43f5e;
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --text-dim: #475569;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
    }}

    body {{
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }}

    /* Header */
    header {{
      background: rgba(18, 24, 36, 0.9);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-color);
      padding: 8px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      z-index: 20;
      flex-wrap: wrap;
    }}

    .brand {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .brand-icon {{
      width: 24px;
      height: 24px;
      fill: var(--accent-cyan);
      filter: drop-shadow(0 0 6px var(--accent-cyan-glow));
    }}

    .brand-title {{
      font-size: 1.1rem;
      font-weight: 800;
      letter-spacing: 1px;
      background: linear-gradient(135deg, #38bdf8, #818cf8);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      text-transform: uppercase;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}

    /* Common Button & Form Elements */
    .btn {{
      background: var(--bg-card);
      color: var(--text-main);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 6px 12px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
    }}

    .btn:hover {{
      background: var(--bg-card-hover);
      border-color: #334155;
    }}

    .btn:active {{
      transform: scale(0.97);
    }}

    .btn-primary {{
      background: linear-gradient(135deg, #0284c7, #0369a1);
      border-color: #38bdf8;
      color: #ffffff;
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.3);
    }}

    .btn-primary:hover {{
      background: linear-gradient(135deg, #0369a1, #075985);
      border-color: #7dd3fc;
    }}

    .btn-mic-active {{
      background: rgba(34, 197, 94, 0.2);
      border-color: var(--accent-green);
      color: #86efac;
      box-shadow: 0 0 12px var(--accent-green-glow);
    }}

    .btn-toggle-active {{
      background: rgba(139, 92, 246, 0.25);
      border-color: var(--accent-purple);
      color: #c4b5fd;
    }}

    .btn-loop-active {{
      background: rgba(245, 158, 11, 0.25);
      border-color: var(--accent-amber);
      color: #fde68a;
    }}

    select.btn {{
      outline: none;
      appearance: none;
      padding-right: 24px;
      background-image: url('data:image/svg+xml;utf8,<svg fill="%2394a3b8" height="20" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><path d="M7 10l5 5 5-5z"/></svg>');
      background-repeat: no-repeat;
      background-position: right 6px center;
    }}

    input[type="file"] {{
      display: none;
    }}

    /* Heads-Up Display (HUD) */
    .hud-bar {{
      background: #0d121c;
      border-bottom: 1px solid var(--border-color);
      padding: 6px 18px;
      display: flex;
      align-items: center;
      justify-content: space-around;
      gap: 12px;
      flex-wrap: wrap;
      font-size: 0.8rem;
    }}

    .hud-stat {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 2px;
    }}

    .hud-label {{
      color: var(--text-muted);
      font-size: 0.68rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .hud-value {{
      font-weight: 700;
      font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
    }}

    .glow-cyan {{
      color: #38bdf8;
      text-shadow: 0 0 8px var(--accent-cyan-glow);
    }}

    .glow-green {{
      color: #4ade80;
      text-shadow: 0 0 8px var(--accent-green-glow);
    }}

    .glow-amber {{
      color: #fbbf24;
      text-shadow: 0 0 8px rgba(245, 158, 11, 0.5);
    }}

    /* Highway Canvas */
    .highway-container {{
      position: relative;
      flex: 1;
      min-height: 380px;
      background: #070a0f;
      overflow: hidden;
    }}

    #highwayCanvas {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      display: block;
    }}

    /* Teleprompter Box */
    .teleprompter-box {{
      background: #0c1018;
      border-top: 1px solid var(--border-color);
      border-bottom: 1px solid var(--border-color);
      padding: 8px 18px;
      text-align: center;
      min-height: 58px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 4px;
    }}

    .current-line-display {{
      font-size: 1.15rem;
      font-weight: 700;
      color: #ffffff;
      letter-spacing: 0.3px;
    }}

    .current-line-display .active-word {{
      color: #4ade80;
      text-shadow: 0 0 10px rgba(74, 222, 128, 0.8);
      font-weight: 800;
      text-decoration: underline;
      text-underline-offset: 4px;
    }}

    .next-line-display {{
      font-size: 0.85rem;
      color: var(--text-muted);
      font-style: italic;
    }}

    /* Control Deck */
    .control-deck {{
      background: rgba(18, 24, 36, 0.95);
      border-top: 1px solid var(--border-color);
      padding: 10px 18px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      z-index: 20;
    }}

    .scrubber-row {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .time-readout {{
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      font-size: 0.78rem;
      color: var(--text-muted);
      min-width: 44px;
    }}

    input[type="range"] {{
      flex: 1;
      height: 6px;
      border-radius: 3px;
      background: #1e293b;
      outline: none;
      cursor: pointer;
      accent-color: #38bdf8;
    }}

    .controls-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }}

    .control-group {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .stem-fader-box {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 4px 10px;
      font-size: 0.75rem;
    }}

    .stem-fader-box input[type="range"] {{
      width: 100px;
      height: 5px;
      accent-color: var(--accent-purple);
    }}

    /* Scorecard Modal */
    .modal-backdrop {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(4, 7, 12, 0.82);
      backdrop-filter: blur(8px);
      z-index: 100;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}

    .modal-backdrop.open {{
      display: flex;
    }}

    .modal-card {{
      background: #121824;
      border: 1px solid #334155;
      border-radius: 14px;
      max-width: 640px;
      width: 100%;
      max-height: 85vh;
      overflow-y: auto;
      padding: 24px;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
      display: flex;
      flex-direction: column;
      gap: 18px;
    }}

    .modal-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid #1e293b;
      padding-bottom: 12px;
    }}

    .modal-title {{
      font-size: 1.25rem;
      font-weight: 800;
      color: #f1f5f9;
    }}

    .score-circle {{
      width: 110px;
      height: 110px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(34, 197, 94, 0.15) 0%, rgba(18, 24, 36, 0.8) 70%);
      border: 3px solid #22c55e;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      margin: 0 auto;
      box-shadow: 0 0 20px var(--accent-green-glow);
    }}

    .score-big {{
      font-size: 2rem;
      font-weight: 900;
      color: #4ade80;
      font-family: ui-monospace, Menlo, monospace;
    }}

    .score-sub {{
      font-size: 0.68rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .metrics-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 10px;
    }}

    .metric-card {{
      background: #0f1520;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 10px;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .phrase-list {{
      display: flex;
      flex-direction: column;
      gap: 6px;
      max-height: 200px;
      overflow-y: auto;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 6px;
      background: #0b1019;
    }}

    .phrase-item {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      font-size: 0.8rem;
      padding: 4px 8px;
      border-radius: 4px;
      background: #121824;
    }}
  </style>
</head>
<body>

  <!-- Top Navigation & Loaders -->
  <header>
    <div class="brand">
      <svg class="brand-icon" viewBox="0 0 24 24">
        <path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z"/>
      </svg>
      <span class="brand-title">Vocal Highway</span>
    </div>

    <!-- Song & Warm-Up Selector -->
    <select id="presetSelect" class="btn" title="Choose demo song or built-in warm-up exercise">
      <option value="song">🎵 Amazing Grace (Public Domain Demo)</option>
      <option value="warmup_5tone">🔥 Warm-Up: 5-Tone Scale (Do-Re-Mi-Fa-Sol)</option>
      <option value="warmup_arpeggio">🔥 Warm-Up: Octave Arpeggio (1-3-5-8-5-3-1)</option>
      <option value="warmup_siren">🔥 Warm-Up: Vocal Sirens (Glissando)</option>
    </select>

    <div class="header-actions">
      <!-- File Loaders -->
      <label class="btn" title="Load custom song_chart.json">
        📁 Chart
        <input type="file" id="chartFileInput" accept=".json">
      </label>
      <label class="btn" title="Load guide vocal stem (vocals.wav)">
        🎙️ Vocals Stem
        <input type="file" id="vocalsFileInput" accept="audio/*,.mp3,.wav,.m4a">
      </label>
      <label class="btn" title="Load backing instrumental stem (no_vocals.wav or song mp3)">
        🎸 Backing Stem
        <input type="file" id="backingFileInput" accept="audio/*,.mp3,.wav,.m4a">
      </label>
      <!-- Mic Activation Button -->
      <button class="btn btn-primary" id="micBtn">
        🎤 Enable Mic
      </button>
      <!-- Scorecard Modal Trigger -->
      <button class="btn" id="scorecardBtn" title="View vocal scorecard & range analytics">
        📊 Scorecard
      </button>
    </div>
  </header>

  <!-- Heads-Up Display (HUD) -->
  <div class="hud-bar">
    <div class="hud-stat">
      <span class="hud-label">Song Time</span>
      <span class="hud-value glow-cyan" id="hudTime">00:00.0</span>
    </div>
    <div class="hud-stat">
      <span class="hud-label">Detected Pitch</span>
      <span class="hud-value" id="hudPitch">-- (0 Hz)</span>
    </div>
    <div class="hud-stat">
      <span class="hud-label">Target Pitch</span>
      <span class="hud-value" id="hudTarget">--</span>
    </div>
    <div class="hud-stat">
      <span class="hud-label">Intonation</span>
      <span class="hud-value glow-cyan" id="hudIntonation">0¢ In Tune</span>
    </div>
    <div class="hud-stat">
      <span class="hud-label">Key Shift</span>
      <span class="hud-value" id="hudKey">0 st</span>
    </div>
    <div class="hud-stat">
      <span class="hud-label">Accuracy</span>
      <span class="hud-value glow-green" id="hudScore">0%</span>
    </div>
    <div class="hud-stat">
      <span class="hud-label">A-B Looper</span>
      <span class="hud-value" id="hudLoopStatus">OFF</span>
    </div>
    <div class="hud-stat">
      <span class="hud-label">Clock Sync</span>
      <span class="hud-value glow-cyan" id="hudSyncStatus">Ready</span>
    </div>
  </div>

  <!-- Interactive Highway Canvas -->
  <div class="highway-container">
    <canvas id="highwayCanvas"></canvas>
  </div>

  <!-- Teleprompter Display -->
  <div class="teleprompter-box">
    <div class="current-line-display" id="currentLineBox">Ready to sing...</div>
    <div class="next-line-display" id="nextLineBox">Upcoming: Amazing grace how sweet the sound</div>
  </div>

  <!-- Bottom Playback Control Deck -->
  <div class="control-deck">
    <!-- Scrubber Row -->
    <div class="scrubber-row">
      <span class="time-readout" id="timeCurrent">00:00</span>
      <input type="range" id="timeScrubber" min="0" max="330" step="0.05" value="0">
      <span class="time-readout" id="timeTotal">05:30</span>
    </div>

    <!-- Controls Row 1: Transport & Looper -->
    <div class="controls-row">
      <div class="control-group">
        <button class="btn btn-primary" id="playPauseBtn" style="min-width: 85px;">
          ▶ Start
        </button>
        <button class="btn" id="restartBtn" title="Restart track">
          ⏮ Reset
        </button>
        <button class="btn" id="skipIntroBtn" title="Skip intro directly to singing">
          ⏩ Skip Intro
        </button>
        <select id="sectionSelect" class="btn" title="Jump to phrase">
          <option value="0">Phrase 1: Start</option>
        </select>
      </div>

      <!-- A-B Practice Looper -->
      <div class="control-group">
        <span style="font-size: 0.75rem; color: var(--text-muted);">Loop:</span>
        <button class="btn" id="loopSetABtn" title="Set Loop Start (A)">[A] Set Start</button>
        <button class="btn" id="loopSetBBtn" title="Set Loop End (B)">[B] Set End</button>
        <button class="btn" id="loopClearBtn" title="Clear A-B Loop">❌ Clear</button>
      </div>
    </div>

    <!-- Controls Row 2: Stems, Key, Speed & Calibration -->
    <div class="controls-row">
      <!-- Dual-Stem Crossfader -->
      <div class="control-group">
        <div class="stem-fader-box" title="Crossfade between backing instrumental and guide vocals">
          <span>🎸 Backing</span>
          <input type="range" id="stemBalanceSlider" min="0" max="100" value="50">
          <span>🎙️ Vocals</span>
        </div>
      </div>

      <!-- Musical Tuning & Features -->
      <div class="control-group">
        <!-- Transpose -->
        <span style="font-size: 0.75rem; color: var(--text-muted);">Key:</span>
        <button class="btn" id="transposeDownBtn" title="Shift down 1 semitone">-</button>
        <span id="transposeDisplay" style="font-weight: 700; font-size: 0.82rem; min-width: 28px; text-align: center;">0</span>
        <button class="btn" id="transposeUpBtn" title="Shift up 1 semitone">+</button>
        <button class="btn" id="autoFitKeyBtn" title="Auto-transpose song to match your natural singing range" style="color: #38bdf8;">
          ✨ Auto-Fit Range
        </button>

        <!-- Highway Scroll Speed -->
        <span style="font-size: 0.75rem; color: var(--text-muted); margin-left: 6px;">Scroll:</span>
        <button class="btn" id="scrollSpeedBtn" title="Cycle highway scrolling speed">
          🏎️ 280 px/s
        </button>

        <!-- Sync Offset Nudge -->
        <span style="font-size: 0.75rem; color: var(--text-muted); margin-left: 6px;">Sync:</span>
        <button class="btn" id="syncMinusBtn" title="Nudge audio sync -50ms">-50ms</button>
        <span id="syncOffsetDisplay" style="font-size: 0.78rem; font-weight: 600; min-width: 48px; text-align: center;">0ms</span>
        <button class="btn" id="syncPlusBtn" title="Nudge audio sync +50ms">+50ms</button>

        <!-- Guide Synth -->
        <button class="btn" id="synthToggleBtn" title="Toggle audio synth note guidance">
          🎹 Guide Synth: OFF
        </button>

        <!-- Playback Speed -->
        <button class="btn" id="speedToggleBtn" title="Toggle playback speed (100% / 75%)">
          ⚡ 100%
        </button>
      </div>
    </div>
  </div>

  <!-- Scorecard Modal -->
  <div id="scorecardModal" class="modal-backdrop">
    <div class="modal-card">
      <div class="modal-header">
        <h2 class="modal-title">🎤 Performance Scorecard</h2>
        <button class="btn" id="closeScorecardBtn">✕ Close</button>
      </div>

      <div class="score-circle">
        <span class="score-big" id="modalAccuracyScore">0%</span>
        <span class="score-sub">Accuracy</span>
      </div>

      <div class="metrics-grid">
        <div class="metric-card">
          <span class="hud-label">Intonation Tendency</span>
          <span class="hud-value glow-cyan" id="modalIntonationBias">0.0¢ Center</span>
        </div>
        <div class="metric-card">
          <span class="hud-label">Your Sung Range</span>
          <span class="hud-value glow-green" id="modalUserRange">-- to --</span>
        </div>
        <div class="metric-card">
          <span class="hud-label">Song Range</span>
          <span class="hud-value" id="modalSongRange">-- to --</span>
        </div>
        <div class="metric-card">
          <span class="hud-label">Recommended Key Shift</span>
          <span class="hud-value glow-amber" id="modalRecKey">0 semitones</span>
        </div>
      </div>

      <div>
        <h4 style="font-size: 0.9rem; margin-bottom: 6px; color: var(--text-muted);">Phrase Breakdown</h4>
        <div class="phrase-list" id="modalPhraseList">
          <!-- Populated dynamically -->
        </div>
      </div>

      <div style="display: flex; gap: 10px; justify-content: flex-end; margin-top: 6px;">
        <button class="btn btn-primary" id="practiceHardestBtn">
          🔁 Practice Hardest Phrase
        </button>
        <button class="btn" id="singAgainBtn">
          ▶ Sing Again
        </button>
      </div>
    </div>
  </div>

  <!-- Audio Elements for Dual-Stem Backing & Vocals -->
  <audio id="backingAudio" preload="auto"></audio>
  <audio id="vocalsAudio" preload="auto"></audio>

  <script>
    /* =====================================================================
       VOCAL HIGHWAY ENGINE — ENHANCED FULL SUITE
       ===================================================================== */
    const PLAYHEAD_X = 180;
    const NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"];

    const SCROLL_SPEEDS = [
      {{ label: "🐢 180 px/s (Chill)", pps: 180 }},
      {{ label: "🏎️ 280 px/s (Default)", pps: 280 }},
      {{ label: "🚀 380 px/s (Fast)", pps: 380 }},
      {{ label: "⚡ 480 px/s (Hero)", pps: 480 }}
    ];
    let scrollSpeedIndex = 1;
    let pixelsPerSecond = SCROLL_SPEEDS[scrollSpeedIndex].pps;

    // Embedded public-domain demo chart
    const DEFAULT_CHART = {demo_chart_json_str.strip()};

    // Built-in warm-up charts
    const WARMUP_CHARTS = {json.dumps(warmup_json)};

    /* =====================================================================
       STATE MANAGEMENT
       ===================================================================== */
    let currentChart = DEFAULT_CHART;
    let isPlaying = false;
    let currentSongTime = 0.0;
    let songDuration = DEFAULT_CHART.duration || 330.0;
    let lastFrameTimestamp = null;
    let playbackSpeed = 1.0;
    let transposeShift = 0;
    let syncOffsetSec = 0.0;
    let guideSynthEnabled = false;

    // A-B Looper State
    let loopA = null;
    let loopB = null;
    let isLoopActive = false;

    // Pitch & Scoring State
    let micStream = null;
    let audioCtx = null;
    let analyserNode = null;
    let timeDomainBuffer = null;
    let detectedPitchHz = 0;
    let rawMidi = null;
    let smoothedMidi = null;
    let prevMidi = null;
    let unvoicedFramesCount = 0;

    let totalScoredFrames = 0;
    let hitScoredFrames = 0;
    let currentActiveWord = null;

    // Continuous Sung Pitch Ribbon History Buffer
    const pitchHistory = []; // {{ time, midi, isHit, cents }}

    // Analytics State
    let sessionMinMidi = null;
    let sessionMaxMidi = null;
    let intonationCentsSum = 0;
    let intonationCentsCount = 0;
    const phraseScores = {{}}; // phraseIdx: {{ hits, total }}

    // Synth Oscillator State
    let guideOsc = null;
    let guideGain = null;

    // Particle FX
    const hitParticles = [];

    /* =====================================================================
       DOM ELEMENTS
       ===================================================================== */
    const canvas = document.getElementById("highwayCanvas");
    const ctx = canvas.getContext("2d");
    const playPauseBtn = document.getElementById("playPauseBtn");
    const restartBtn = document.getElementById("restartBtn");
    const skipIntroBtn = document.getElementById("skipIntroBtn");
    const timeScrubber = document.getElementById("timeScrubber");
    const timeCurrent = document.getElementById("timeCurrent");
    const timeTotal = document.getElementById("timeTotal");
    const sectionSelect = document.getElementById("sectionSelect");
    const presetSelect = document.getElementById("presetSelect");

    const hudTime = document.getElementById("hudTime");
    const hudPitch = document.getElementById("hudPitch");
    const hudTarget = document.getElementById("hudTarget");
    const hudIntonation = document.getElementById("hudIntonation");
    const hudKey = document.getElementById("hudKey");
    const hudScore = document.getElementById("hudScore");
    const hudLoopStatus = document.getElementById("hudLoopStatus");
    const hudSyncStatus = document.getElementById("hudSyncStatus");

    const currentLineBox = document.getElementById("currentLineBox");
    const nextLineBox = document.getElementById("nextLineBox");

    const chartFileInput = document.getElementById("chartFileInput");
    const vocalsFileInput = document.getElementById("vocalsFileInput");
    const backingFileInput = document.getElementById("backingFileInput");
    const backingAudio = document.getElementById("backingAudio");
    const vocalsAudio = document.getElementById("vocalsAudio");
    const stemBalanceSlider = document.getElementById("stemBalanceSlider");
    const micBtn = document.getElementById("micBtn");

    const loopSetABtn = document.getElementById("loopSetABtn");
    const loopSetBBtn = document.getElementById("loopSetBBtn");
    const loopClearBtn = document.getElementById("loopClearBtn");

    const transposeDownBtn = document.getElementById("transposeDownBtn");
    const transposeUpBtn = document.getElementById("transposeUpBtn");
    const transposeDisplay = document.getElementById("transposeDisplay");
    const autoFitKeyBtn = document.getElementById("autoFitKeyBtn");
    const synthToggleBtn = document.getElementById("synthToggleBtn");
    const speedToggleBtn = document.getElementById("speedToggleBtn");

    const scrollSpeedBtn = document.getElementById("scrollSpeedBtn");
    const syncMinusBtn = document.getElementById("syncMinusBtn");
    const syncPlusBtn = document.getElementById("syncPlusBtn");
    const syncOffsetDisplay = document.getElementById("syncOffsetDisplay");

    // Modal elements
    const scorecardBtn = document.getElementById("scorecardBtn");
    const scorecardModal = document.getElementById("scorecardModal");
    const closeScorecardBtn = document.getElementById("closeScorecardBtn");
    const modalAccuracyScore = document.getElementById("modalAccuracyScore");
    const modalIntonationBias = document.getElementById("modalIntonationBias");
    const modalUserRange = document.getElementById("modalUserRange");
    const modalSongRange = document.getElementById("modalSongRange");
    const modalRecKey = document.getElementById("modalRecKey");
    const modalPhraseList = document.getElementById("modalPhraseList");
    const practiceHardestBtn = document.getElementById("practiceHardestBtn");
    const singAgainBtn = document.getElementById("singAgainBtn");

    /* =====================================================================
       CANVAS SIZING & COORDINATES
       ===================================================================== */
    let canvasWidth = 0;
    let canvasHeight = 0;
    let minPitchMidi = 48;
    let maxPitchMidi = 84;

    function resizeCanvas() {{
      const dpr = window.devicePixelRatio || 1;
      const rect = canvas.parentElement.getBoundingClientRect();
      canvasWidth = rect.width;
      canvasHeight = rect.height;

      canvas.width = Math.floor(canvasWidth * dpr);
      canvas.height = Math.floor(canvasHeight * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }}
    window.addEventListener("resize", resizeCanvas);

    function midiToY(midi) {{
      const topPadding = 50;
      const bottomPadding = 50;
      const effectiveHeight = canvasHeight - topPadding - bottomPadding;
      const ratio = (midi - minPitchMidi) / (maxPitchMidi - minPitchMidi);
      return canvasHeight - bottomPadding - (ratio * effectiveHeight);
    }}

    function midiToNoteName(midi) {{
      if (midi == null || isNaN(midi)) return "--";
      const rounded = Math.round(midi);
      const note = NOTE_NAMES[((rounded % 12) + 12) % 12];
      const octave = Math.floor(rounded / 12) - 1;
      const cents = Math.round((midi - rounded) * 100);
      const centsStr = cents >= 0 ? `+${{cents}}¢` : `${{cents}}¢`;
      return `${{note}}${{octave}} (${{centsStr}})`;
    }}

    function midiToBareNote(midi) {{
      if (midi == null || isNaN(midi)) return "--";
      const rounded = Math.round(midi);
      const note = NOTE_NAMES[((rounded % 12) + 12) % 12];
      const octave = Math.floor(rounded / 12) - 1;
      return `${{note}}${{octave}}`;
    }}

    function formatTime(seconds) {{
      const mins = Math.floor(seconds / 60);
      const secs = Math.floor(seconds % 60);
      return `${{mins.toString().padStart(2, "0")}}:${{secs.toString().padStart(2, "0")}}`;
    }}

    function formatTimeDec(seconds) {{
      const mins = Math.floor(seconds / 60);
      const secs = (seconds % 60).toFixed(1);
      return `${{mins.toString().padStart(2, "0")}}:${{secs.padStart(4, "0")}}`;
    }}

    /* =====================================================================
       CHART DATA & SECTION POPULATION
       ===================================================================== */
    function loadChartData(chart) {{
      currentChart = chart;
      songDuration = chart.duration || 330.0;
      timeScrubber.max = songDuration;
      timeTotal.textContent = formatTime(songDuration);

      let lowest = 127;
      let highest = 0;
      (chart.lines || []).forEach(line => {{
        (line.words || []).forEach(w => {{
          if (w.midi) {{
            lowest = Math.min(lowest, w.midi);
            highest = Math.max(highest, w.midi);
          }}
          if (w.subNotes) {{
            w.subNotes.forEach(sn => {{
              lowest = Math.min(lowest, sn.midi);
              highest = Math.max(highest, sn.midi);
            }});
          }}
        }});
      }});

      if (lowest < highest) {{
        minPitchMidi = Math.max(40, lowest - 3);
        maxPitchMidi = Math.min(88, highest + 3);
      }}

      sectionSelect.innerHTML = "";
      (chart.lines || []).forEach((line, idx) => {{
        const opt = document.createElement("option");
        opt.value = line.startTime || 0;
        opt.textContent = `${{line.section || `Phrase ${{idx + 1}}`}} (${{formatTime(line.startTime)}}): ${{line.fullLine.slice(0, 24)}}...`;
        sectionSelect.appendChild(opt);
      }});

      // Reset scores and looper
      clearLoop();
      resetPlayhead();
    }}

    /* =====================================================================
       WEB AUDIO API & AUTOCORRELATION PITCH DETECTOR
       ===================================================================== */
    async function initAudioContext() {{
      if (!audioCtx) {{
        const AudioContextClass = window.AudioContext || window.webkitAudioContext;
        audioCtx = new AudioContextClass();
      }}
      if (audioCtx.state === "suspended") {{
        await audioCtx.resume();
      }}
    }}

    async function toggleMicrophone() {{
      await initAudioContext();
      if (micStream) {{
        micStream.getTracks().forEach(t => t.stop());
        micStream = null;
        micBtn.textContent = "🎤 Enable Mic";
        micBtn.classList.remove("btn-mic-active");
        smoothedMidi = null;
        return;
      }}

      try {{
        micStream = await navigator.mediaDevices.getUserMedia({{
          audio: {{
            echoCancellation: false,
            noiseSuppression: false,
            autoGainControl: false
          }}
        }});
        const source = audioCtx.createMediaStreamSource(micStream);
        analyserNode = audioCtx.createAnalyser();
        analyserNode.fftSize = 2048;
        source.connect(analyserNode);

        timeDomainBuffer = new Float32Array(analyserNode.fftSize);
        micBtn.textContent = "🎤 Mic: ON";
        micBtn.classList.add("btn-mic-active");
      }} catch (err) {{
        console.error("Microphone access error:", err);
        alert("Microphone error: " + err.message);
      }}
    }}

    function detectPitch() {{
      if (!analyserNode || !timeDomainBuffer) return null;
      analyserNode.getFloatTimeDomainData(timeDomainBuffer);

      const bufferLen = timeDomainBuffer.length;
      let rms = 0;
      for (let i = 0; i < bufferLen; i++) {{
        rms += timeDomainBuffer[i] * timeDomainBuffer[i];
      }}
      rms = Math.sqrt(rms / bufferLen);

      if (rms < 0.012) {{
        unvoicedFramesCount++;
        if (unvoicedFramesCount > 6) return null;
        return smoothedMidi;
      }}
      unvoicedFramesCount = 0;

      const sampleRate = audioCtx.sampleRate;
      const minPeriod = Math.floor(sampleRate / 1050);
      const maxPeriod = Math.floor(sampleRate / 75);

      let bestCorrelation = -1;
      let bestTau = -1;

      for (let tau = minPeriod; tau <= maxPeriod; tau++) {{
        let sum = 0;
        for (let i = 0; i < bufferLen - tau; i++) {{
          sum += timeDomainBuffer[i] * timeDomainBuffer[i + tau];
        }}
        if (sum > bestCorrelation) {{
          bestCorrelation = sum;
          bestTau = tau;
        }}
      }}

      if (bestTau > 0 && bestCorrelation > 0.05) {{
        let delta = 0;
        if (bestTau > minPeriod && bestTau < maxPeriod) {{
          let cPrev = 0, cNext = 0;
          for (let i = 0; i < bufferLen - (bestTau + 1); i++) {{
            cPrev += timeDomainBuffer[i] * timeDomainBuffer[i + (bestTau - 1)];
            cNext += timeDomainBuffer[i] * timeDomainBuffer[i + (bestTau + 1)];
          }}
          const denom = 2 * (2 * bestCorrelation - cPrev - cNext);
          if (denom !== 0) delta = (cNext - cPrev) / denom;
        }}

        const interpolatedPeriod = bestTau + delta;
        const freq = sampleRate / interpolatedPeriod;

        if (freq >= 75 && freq <= 1050) {{
          detectedPitchHz = freq;
          return 69 + 12 * Math.log2(freq / 440.0);
        }}
      }}

      return null;
    }}

    /* =====================================================================
       AUDIO GUIDE SYNTHESIZER
       ===================================================================== */
    function updateGuideSynth(activeTargetMidi) {{
      if (!guideSynthEnabled || !audioCtx) {{
        if (guideGain && audioCtx) {{
          guideGain.gain.setTargetAtTime(0, audioCtx.currentTime, 0.02);
        }}
        return;
      }}

      if (activeTargetMidi != null && isPlaying) {{
        const freq = 440.0 * Math.pow(2, (activeTargetMidi - 69) / 12);
        if (!guideOsc) {{
          guideOsc = audioCtx.createOscillator();
          guideGain = audioCtx.createGain();
          guideOsc.type = "triangle";
          guideGain.gain.setValueAtTime(0, audioCtx.currentTime);
          guideOsc.connect(guideGain);
          guideGain.connect(audioCtx.destination);
          guideOsc.start();
        }}
        guideOsc.frequency.setTargetAtTime(freq, audioCtx.currentTime, 0.015);
        guideGain.gain.setTargetAtTime(0.12, audioCtx.currentTime, 0.03);
      }} else {{
        if (guideGain && audioCtx) {{
          guideGain.gain.setTargetAtTime(0, audioCtx.currentTime, 0.02);
        }}
      }}
    }}

    /* =====================================================================
       DUAL-STEM AUDIO MIXER & TIME CLOCK
       ===================================================================== */
    function hasBackingTrack() {{
      return backingAudio && backingAudio.src && backingAudio.src !== window.location.href && !backingAudio.error;
    }}

    function hasVocalsTrack() {{
      return vocalsAudio && vocalsAudio.src && vocalsAudio.src !== window.location.href && !vocalsAudio.error;
    }}

    function updateStemVolume() {{
      const bal = parseFloat(stemBalanceSlider.value); // 0 to 100
      let backingVol = 1.0;
      let vocalsVol = 1.0;

      if (bal <= 50) {{
        vocalsVol = bal / 50.0;
        backingVol = 1.0;
      }} else {{
        vocalsVol = 1.0;
        backingVol = (100.0 - bal) / 50.0;
      }}

      if (hasBackingTrack()) backingAudio.volume = backingVol;
      if (hasVocalsTrack()) vocalsAudio.volume = vocalsVol;
    }}
    stemBalanceSlider.addEventListener("input", updateStemVolume);

    function syncStemPlayback() {{
      if (hasBackingTrack()) {{
        backingAudio.currentTime = Math.max(0, currentSongTime);
        backingAudio.playbackRate = playbackSpeed;
        if (isPlaying && backingAudio.paused) backingAudio.play().catch(e => console.warn(e));
        else if (!isPlaying && !backingAudio.paused) backingAudio.pause();
      }}
      if (hasVocalsTrack()) {{
        vocalsAudio.currentTime = Math.max(0, currentSongTime);
        vocalsAudio.playbackRate = playbackSpeed;
        if (isPlaying && vocalsAudio.paused) vocalsAudio.play().catch(e => console.warn(e));
        else if (!isPlaying && !vocalsAudio.paused) vocalsAudio.pause();
      }}
    }}

    function togglePlay() {{
      initAudioContext();
      isPlaying = !isPlaying;

      if (isPlaying) {{
        playPauseBtn.textContent = "❚❚ Pause";
        playPauseBtn.classList.remove("btn-primary");
        lastFrameTimestamp = performance.now();
        syncStemPlayback();
      }} else {{
        playPauseBtn.textContent = "▶ Start";
        playPauseBtn.classList.add("btn-primary");
        syncStemPlayback();
        updateGuideSynth(null);
      }}
    }}

    function resetPlayhead() {{
      currentSongTime = 0.0;
      timeScrubber.value = 0;
      totalScoredFrames = 0;
      hitScoredFrames = 0;
      pitchHistory.length = 0;
      hudScore.textContent = "0%";
      syncStemPlayback();
      updateTeleprompter();
    }}

    function seekTo(targetTime) {{
      currentSongTime = Math.max(0, Math.min(songDuration, targetTime));
      timeScrubber.value = currentSongTime;
      syncStemPlayback();
      updateTeleprompter();
    }}

    /* =====================================================================
       A-B PRACTICE LOOPER
       ===================================================================== */
    function setLoopA() {{
      loopA = currentSongTime;
      loopSetABtn.textContent = `[A] ${{formatTime(loopA)}}`;
      loopSetABtn.classList.add("btn-loop-active");
      if (loopB != null && loopB > loopA) {{
        isLoopActive = true;
      }}
      updateLoopUI();
    }}

    function setLoopB() {{
      loopB = currentSongTime;
      loopSetBBtn.textContent = `[B] ${{formatTime(loopB)}}`;
      loopSetBBtn.classList.add("btn-loop-active");
      if (loopA != null && loopB > loopA) {{
        isLoopActive = true;
      }}
      updateLoopUI();
    }}

    function clearLoop() {{
      loopA = null;
      loopB = null;
      isLoopActive = false;
      loopSetABtn.textContent = "[A] Set Start";
      loopSetBBtn.textContent = "[B] Set End";
      loopSetABtn.classList.remove("btn-loop-active");
      loopSetBBtn.classList.remove("btn-loop-active");
      updateLoopUI();
    }}

    function updateLoopUI() {{
      if (isLoopActive && loopA != null && loopB != null) {{
        hudLoopStatus.textContent = `${{formatTime(loopA)}} ⇄ ${{formatTime(loopB)}}`;
        hudLoopStatus.className = "hud-value glow-amber";
      }} else {{
        hudLoopStatus.textContent = "OFF";
        hudLoopStatus.className = "hud-value";
      }}
    }}

    loopSetABtn.addEventListener("click", setLoopA);
    loopSetBBtn.addEventListener("click", setLoopB);
    loopClearBtn.addEventListener("click", clearLoop);

    /* =====================================================================
       TELEPROMPTER & LYRICS DISPLAY
       ===================================================================== */
    function updateTeleprompter() {{
      const lines = currentChart.lines || [];
      let activeLine = null;
      let nextLine = null;

      for (let i = 0; i < lines.length; i++) {{
        const line = lines[i];
        const lineEnd = line.words && line.words.length
          ? line.words[line.words.length - 1].start + line.words[line.words.length - 1].dur + 0.6
          : line.startTime + 3.0;

        if (currentSongTime >= line.startTime - 0.4 && currentSongTime <= lineEnd) {{
          activeLine = line;
          nextLine = lines[i + 1] || null;
          break;
        }} else if (currentSongTime < line.startTime) {{
          if (!nextLine) {{
            activeLine = null;
            nextLine = line;
          }}
          break;
        }}
      }}

      if (activeLine) {{
        let htmlWords = [];
        (activeLine.words || []).forEach(w => {{
          const isCurrent = currentSongTime >= w.start && currentSongTime <= w.start + w.dur;
          if (isCurrent) {{
            htmlWords.push(`<span class="active-word">${{w.text}}</span>`);
          }} else {{
            htmlWords.push(w.text);
          }}
        }});
        currentLineBox.innerHTML = htmlWords.join(" ");
        nextLineBox.textContent = nextLine ? `Upcoming: ${{nextLine.fullLine}}` : "";
      }} else {{
        const firstStart = lines.length > 0 ? (lines[0].startTime || 0) : 0;
        currentLineBox.textContent = (firstStart > 0.5 && currentSongTime < firstStart - 0.2)
          ? `Intro (Singing starts at ${{formatTimeDec(firstStart)}})`
          : "---";
        nextLineBox.textContent = nextLine ? `Upcoming: ${{nextLine.fullLine}}` : "";
      }}
    }}

    /* =====================================================================
       PARTICLE VISUAL FX
       ===================================================================== */
    function spawnHitParticles(x, y) {{
      for (let i = 0; i < 3; i++) {{
        hitParticles.push({{
          x: x,
          y: y,
          vx: (Math.random() - 0.5) * 5,
          vy: (Math.random() - 0.5) * 5,
          radius: Math.random() * 3 + 1.5,
          life: 1.0,
          color: Math.random() > 0.3 ? "#22c55e" : "#86efac"
        }});
      }}
    }}

    function renderParticles() {{
      for (let i = hitParticles.length - 1; i >= 0; i--) {{
        const p = hitParticles[i];
        p.x += p.vx;
        p.y += p.vy;
        p.life -= 0.04;
        if (p.life <= 0) {{
          hitParticles.splice(i, 1);
          continue;
        }}
        ctx.save();
        ctx.globalAlpha = p.life;
        ctx.fillStyle = p.color;
        ctx.shadowColor = "#22c55e";
        ctx.shadowBlur = 6;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
      }}
    }}

    /* =====================================================================
       CONTINUOUS SUNG PITCH RIBBON RENDERER (SingStar / Smule Style)
       ===================================================================== */
    function renderPitchRibbon(effectiveSongTime) {{
      if (pitchHistory.length < 2) return;

      // Group contiguous voiced points (time gap <= 0.15s)
      const segments = [];
      let currentSegment = [];

      for (let i = 0; i < pitchHistory.length; i++) {{
        const pt = pitchHistory[i];
        const prevPt = pitchHistory[i - 1];
        if (prevPt && Math.abs(pt.time - prevPt.time) > 0.15) {{
          if (currentSegment.length > 0) {{
            segments.push(currentSegment);
            currentSegment = [];
          }}
        }}
        currentSegment.push(pt);
      }}
      if (currentSegment.length > 0) {{
        segments.push(currentSegment);
      }}

      ctx.save();
      ctx.lineCap = "round";
      ctx.lineJoin = "round";

      segments.forEach(seg => {{
        if (seg.length < 2) return;
        const coords = seg.map(pt => ({{
          x: PLAYHEAD_X + (pt.time - effectiveSongTime) * pixelsPerSecond,
          y: midiToY(pt.midi + transposeShift),
          isHit: pt.isHit
        }}));

        // 1. Soft glowing halo underlay
        ctx.beginPath();
        ctx.moveTo(coords[0].x, coords[0].y);
        for (let j = 1; j < coords.length; j++) {{
          const xc = (coords[j].x + coords[j - 1].x) / 2;
          const yc = (coords[j].y + coords[j - 1].y) / 2;
          ctx.quadraticCurveTo(coords[j - 1].x, coords[j - 1].y, xc, yc);
        }}
        ctx.lineTo(coords[coords.length - 1].x, coords[coords.length - 1].y);
        ctx.strokeStyle = "rgba(6, 182, 212, 0.2)";
        ctx.lineWidth = 12;
        ctx.stroke();

        // 2. Crisp neon core ribbon
        ctx.beginPath();
        ctx.moveTo(coords[0].x, coords[0].y);
        for (let j = 1; j < coords.length; j++) {{
          const xc = (coords[j].x + coords[j - 1].x) / 2;
          const yc = (coords[j].y + coords[j - 1].y) / 2;
          ctx.quadraticCurveTo(coords[j - 1].x, coords[j - 1].y, xc, yc);
        }}
        ctx.lineTo(coords[coords.length - 1].x, coords[coords.length - 1].y);

        const lastPoint = seg[seg.length - 1];
        ctx.strokeStyle = lastPoint.isHit ? "#22c55e" : "#06b6d4";
        ctx.shadowColor = lastPoint.isHit ? "#22c55e" : "#06b6d4";
        ctx.shadowBlur = 10;
        ctx.lineWidth = 4;
        ctx.stroke();
      }});

      ctx.restore();
    }}

    /* =====================================================================
       HIGHWAY RENDER LOOP WITH PLL TIME SYNC & A-B ENFORCEMENT
       ===================================================================== */
    function render(timestamp) {{
      requestAnimationFrame(render);

      if (lastFrameTimestamp == null) lastFrameTimestamp = timestamp;
      const dt = Math.min(0.1, (timestamp - lastFrameTimestamp) / 1000.0);
      lastFrameTimestamp = timestamp;

      // Phase-Locked Loop (PLL) Time Progression:
      if (isPlaying) {{
        if (hasBackingTrack() && !backingAudio.paused) {{
          const audioTime = backingAudio.currentTime;
          const drift = audioTime - currentSongTime;

          if (Math.abs(drift) > 0.25 || backingAudio.seeking) {{
            currentSongTime = audioTime;
          }} else {{
            currentSongTime += (dt * playbackSpeed) + (drift * 0.15);
          }}
          hudSyncStatus.textContent = "Audio Locked";
          hudSyncStatus.className = "hud-value glow-green";
        }} else {{
          currentSongTime += dt * playbackSpeed;
          hudSyncStatus.textContent = "Internal Clock";
          hudSyncStatus.className = "hud-value glow-cyan";
        }}

        // A-B Looper check
        if (isLoopActive && loopA != null && loopB != null && loopB > loopA) {{
          if (currentSongTime >= loopB) {{
            seekTo(loopA);
          }}
        }}

        // Song end check
        if (currentSongTime >= songDuration) {{
          currentSongTime = songDuration;
          togglePlay();
          openScorecard();
        }}
        timeScrubber.value = currentSongTime;
      }}

      timeCurrent.textContent = formatTime(currentSongTime);
      hudTime.textContent = formatTimeDec(currentSongTime);

      const rawDetected = detectPitch();
      if (rawDetected != null) {{
        rawMidi = rawDetected;
        smoothedMidi = prevMidi != null ? (0.65 * prevMidi + 0.35 * rawMidi) : rawMidi;
        prevMidi = smoothedMidi;

        // Track voice range
        if (sessionMinMidi == null || smoothedMidi < sessionMinMidi) sessionMinMidi = Math.round(smoothedMidi);
        if (sessionMaxMidi == null || smoothedMidi > sessionMaxMidi) sessionMaxMidi = Math.round(smoothedMidi);
      }} else {{
        if (prevMidi != null) {{
          smoothedMidi = null;
          prevMidi = null;
        }}
      }}

      ctx.clearRect(0, 0, canvasWidth, canvasHeight);

      // 1. Draw Semitone Lanes
      ctx.lineWidth = 1;
      for (let m = minPitchMidi; m <= maxPitchMidi; m++) {{
        const y = midiToY(m);
        const isOctaveC = m % 12 === 0;
        const noteIndex = ((m % 12) + 12) % 12;
        const isWhiteKey = ![1, 3, 6, 8, 10].includes(noteIndex);

        if (isOctaveC) {{
          ctx.strokeStyle = "rgba(6, 182, 212, 0.4)";
          ctx.lineWidth = 1.5;
        }} else if (isWhiteKey) {{
          ctx.strokeStyle = "rgba(255, 255, 255, 0.05)";
          ctx.lineWidth = 1;
        }} else {{
          ctx.strokeStyle = "rgba(0, 0, 0, 0.25)";
          ctx.lineWidth = 1;
        }}

        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(canvasWidth, y);
        ctx.stroke();

        if (isOctaveC || isWhiteKey) {{
          ctx.fillStyle = isOctaveC ? "#38bdf8" : "rgba(148, 163, 184, 0.4)";
          ctx.font = isOctaveC ? "bold 11px system-ui" : "9px system-ui";
          ctx.textAlign = "left";
          ctx.textBaseline = "middle";
          const label = `${{NOTE_NAMES[noteIndex]}}${{Math.floor(m / 12) - 1}}`;
          ctx.fillText(label, 8, y);
        }}
      }}

      // 2. Draw A-B Loop Region Highlights
      const effectiveSongTime = currentSongTime + syncOffsetSec;
      if (loopA != null) {{
        const xA = PLAYHEAD_X + (loopA - effectiveSongTime) * pixelsPerSecond;
        ctx.save();
        ctx.beginPath();
        ctx.moveTo(xA, 0);
        ctx.lineTo(xA, canvasHeight);
        ctx.strokeStyle = "#22c55e";
        ctx.lineWidth = 2;
        ctx.setLineDash([6, 4]);
        ctx.stroke();
        ctx.fillStyle = "#22c55e";
        ctx.font = "bold 10px system-ui";
        ctx.fillText("[A] LOOP", xA + 4, 30);
        ctx.restore();
      }}

      if (loopB != null) {{
        const xB = PLAYHEAD_X + (loopB - effectiveSongTime) * pixelsPerSecond;
        ctx.save();
        ctx.beginPath();
        ctx.moveTo(xB, 0);
        ctx.lineTo(xB, canvasHeight);
        ctx.strokeStyle = "#f59e0b";
        ctx.lineWidth = 2;
        ctx.setLineDash([6, 4]);
        ctx.stroke();
        ctx.fillStyle = "#f59e0b";
        ctx.font = "bold 10px system-ui";
        ctx.fillText("[B] LOOP", xB - 48, 30);
        ctx.restore();
      }}

      if (loopA != null && loopB != null && loopB > loopA) {{
        const xA = PLAYHEAD_X + (loopA - effectiveSongTime) * pixelsPerSecond;
        const xB = PLAYHEAD_X + (loopB - effectiveSongTime) * pixelsPerSecond;
        ctx.save();
        ctx.fillStyle = "rgba(56, 189, 248, 0.06)";
        ctx.fillRect(xA, 0, xB - xA, canvasHeight);
        ctx.restore();
      }}

      // 3. Draw Target Vocal Highway Bars (with melisma sub-notes support)
      let targetMidiAtPlayhead = null;
      currentActiveWord = null;
      let activePhraseIdx = null;

      (currentChart.lines || []).forEach((line, lIdx) => {{
        if (!phraseScores[lIdx]) phraseScores[lIdx] = {{ hits: 0, total: 0 }};

        (line.words || []).forEach(word => {{
          const isWordAtPlayhead = (effectiveSongTime >= word.start - 0.08 && effectiveSongTime <= word.start + word.dur + 0.08);
          if (isWordAtPlayhead) {{
            currentActiveWord = word;
            activePhraseIdx = lIdx;
          }}

          // Check if word has melisma sub-notes
          if (word.subNotes && word.subNotes.length > 1) {{
            word.subNotes.forEach((sn, snIdx) => {{
              const subX = PLAYHEAD_X + (sn.start - effectiveSongTime) * pixelsPerSecond;
              const subW = Math.max(20, sn.dur * pixelsPerSecond - 2);
              const subMidi = sn.midi + transposeShift;
              const subY = midiToY(subMidi);
              const barHeight = 22;

              const isSubAtPlayhead = (effectiveSongTime >= sn.start - 0.05 && effectiveSongTime <= sn.start + sn.dur + 0.05);
              if (isSubAtPlayhead) {{
                targetMidiAtPlayhead = subMidi;
              }}

              if (subX + subW < -50 || subX > canvasWidth + 50) return;

              const isSubHit = isSubAtPlayhead && smoothedMidi != null && Math.abs(smoothedMidi - subMidi) <= 0.7;

              ctx.save();
              ctx.beginPath();
              ctx.roundRect(subX, subY - barHeight / 2, subW, barHeight, 5);

              const grad = ctx.createLinearGradient(subX, subY, subX + subW, subY);
              if (isSubHit) {{
                grad.addColorStop(0, "#22c55e");
                grad.addColorStop(1, "#16a34a");
                ctx.shadowColor = "#22c55e";
                ctx.shadowBlur = 12;
                spawnHitParticles(PLAYHEAD_X, subY);
              }} else if (isSubAtPlayhead) {{
                grad.addColorStop(0, "#38bdf8");
                grad.addColorStop(1, "#0284c7");
                ctx.shadowColor = "rgba(56, 189, 248, 0.5)";
                ctx.shadowBlur = 8;
              }} else {{
                grad.addColorStop(0, "rgba(51, 65, 85, 0.88)");
                grad.addColorStop(1, "rgba(30, 41, 59, 0.88)");
              }}

              ctx.fillStyle = grad;
              ctx.fill();
              ctx.strokeStyle = isSubHit ? "#86efac" : (isSubAtPlayhead ? "#7dd3fc" : "rgba(100, 116, 139, 0.5)");
              ctx.lineWidth = isSubHit ? 2 : 1;
              ctx.stroke();

              ctx.shadowBlur = 0;
              ctx.fillStyle = isSubHit ? "#ffffff" : "#f8fafc";
              ctx.font = "bold 10px system-ui";
              ctx.textAlign = "center";
              ctx.textBaseline = "middle";
              // Only draw word text on first sub-note or if wide enough
              const displayText = snIdx === 0 ? word.text : "·";
              ctx.fillText(displayText, subX + subW / 2, subY);

              ctx.font = "8px system-ui";
              ctx.fillStyle = "rgba(226, 232, 240, 0.7)";
              const noteText = NOTE_NAMES[((subMidi % 12) + 12) % 12];
              ctx.fillText(noteText, subX + subW / 2, subY - barHeight / 2 - 6);
              ctx.restore();
            }});
          }} else {{
            // Standard single-note word bar
            const x = PLAYHEAD_X + (word.start - effectiveSongTime) * pixelsPerSecond;
            const width = Math.max(28, word.dur * pixelsPerSecond - 4);
            const effectiveMidi = word.midi + transposeShift;
            const y = midiToY(effectiveMidi);
            const barHeight = 24;

            if (isWordAtPlayhead) {{
              targetMidiAtPlayhead = effectiveMidi;
            }}

            if (x + width < -50 || x > canvasWidth + 50) return;

            const isHit = isWordAtPlayhead && smoothedMidi != null && Math.abs(smoothedMidi - effectiveMidi) <= 0.7;

            ctx.save();
            ctx.beginPath();
            ctx.roundRect(x, y - barHeight / 2, width, barHeight, 6);

            const grad = ctx.createLinearGradient(x, y, x + width, y);
            if (isHit) {{
              grad.addColorStop(0, "#22c55e");
              grad.addColorStop(1, "#16a34a");
              ctx.shadowColor = "#22c55e";
              ctx.shadowBlur = 14;
              spawnHitParticles(PLAYHEAD_X, y);
            }} else if (isWordAtPlayhead) {{
              grad.addColorStop(0, "#38bdf8");
              grad.addColorStop(1, "#0284c7");
              ctx.shadowColor = "rgba(56, 189, 248, 0.5)";
              ctx.shadowBlur = 10;
            }} else {{
              grad.addColorStop(0, "rgba(51, 65, 85, 0.88)");
              grad.addColorStop(1, "rgba(30, 41, 59, 0.88)");
            }}

            ctx.fillStyle = grad;
            ctx.fill();
            ctx.strokeStyle = isHit ? "#86efac" : (isWordAtPlayhead ? "#7dd3fc" : "rgba(100, 116, 139, 0.5)");
            ctx.lineWidth = isHit ? 2 : 1;
            ctx.stroke();

            ctx.shadowBlur = 0;
            ctx.fillStyle = isHit ? "#ffffff" : "#f8fafc";
            ctx.font = "bold 11px system-ui";
            ctx.textAlign = "center";
            ctx.textBaseline = "middle";
            ctx.fillText(word.text, x + width / 2, y);

            ctx.font = "9px system-ui";
            ctx.fillStyle = "rgba(226, 232, 240, 0.75)";
            const noteText = NOTE_NAMES[((effectiveMidi % 12) + 12) % 12];
            ctx.fillText(noteText, x + width / 2, y - barHeight / 2 - 7);
            ctx.restore();
          }}
        }});
      }});

      // 4. Update Continuous Sung Pitch Ribbon Buffer
      const isCurrentHit = (targetMidiAtPlayhead != null && smoothedMidi != null && Math.abs(smoothedMidi - targetMidiAtPlayhead) <= 0.7);
      let centsDiff = 0;
      if (targetMidiAtPlayhead != null && smoothedMidi != null) {{
        centsDiff = Math.round((smoothedMidi - targetMidiAtPlayhead) * 100);
        intonationCentsSum += centsDiff;
        intonationCentsCount++;
      }}

      if (smoothedMidi != null) {{
        pitchHistory.push({{
          time: effectiveSongTime,
          midi: smoothedMidi,
          isHit: isCurrentHit,
          cents: centsDiff
        }});
      }}
      while (pitchHistory.length > 0 && effectiveSongTime - pitchHistory[0].time > 3.5) {{
        pitchHistory.shift();
      }}

      // Render Continuous Pitch Ribbon
      renderPitchRibbon(effectiveSongTime);

      // 5. Score Evaluation
      if (isPlaying && targetMidiAtPlayhead != null) {{
        totalScoredFrames++;
        if (activePhraseIdx != null && phraseScores[activePhraseIdx]) {{
          phraseScores[activePhraseIdx].total++;
        }}
        if (isCurrentHit) {{
          hitScoredFrames++;
          if (activePhraseIdx != null && phraseScores[activePhraseIdx]) {{
            phraseScores[activePhraseIdx].hits++;
          }}
        }}
        const pct = Math.round((hitScoredFrames / Math.max(1, totalScoredFrames)) * 100);
        hudScore.textContent = `${{pct}}%`;
      }}

      hudTarget.textContent = targetMidiAtPlayhead ? midiToNoteName(targetMidiAtPlayhead) : "--";
      updateGuideSynth(targetMidiAtPlayhead);

      // 6. Draw SING NOW Vertical Playhead Line (x = 180)
      ctx.save();
      ctx.beginPath();
      ctx.moveTo(PLAYHEAD_X, 0);
      ctx.lineTo(PLAYHEAD_X, canvasHeight);
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2.5;
      ctx.shadowColor = "rgba(56, 189, 248, 0.85)";
      ctx.shadowBlur = 12;
      ctx.stroke();

      ctx.fillStyle = "#38bdf8";
      ctx.shadowBlur = 6;
      ctx.font = "bold 10px system-ui";
      ctx.textAlign = "center";
      ctx.fillText("▼ SING NOW", PLAYHEAD_X, 18);
      ctx.restore();

      // 7. Draw Voice Cursor & Intonation Cents Meter Badge
      if (smoothedMidi != null) {{
        const cursorY = midiToY(smoothedMidi);
        hudPitch.textContent = `${{midiToNoteName(smoothedMidi)}} (${{detectedPitchHz.toFixed(1)}} Hz)`;

        ctx.save();
        // Cursor outer pulse ring
        ctx.beginPath();
        ctx.arc(PLAYHEAD_X, cursorY, 14, 0, Math.PI * 2);
        ctx.fillStyle = isCurrentHit ? "rgba(34, 197, 94, 0.25)" : "rgba(56, 189, 248, 0.25)";
        ctx.fill();

        // Cursor core dot
        ctx.beginPath();
        ctx.arc(PLAYHEAD_X, cursorY, 7, 0, Math.PI * 2);
        ctx.fillStyle = isCurrentHit ? "#22c55e" : "#38bdf8";
        ctx.shadowColor = isCurrentHit ? "#22c55e" : "#38bdf8";
        ctx.shadowBlur = 15;
        ctx.fill();

        // Intonation Cents Badge
        if (targetMidiAtPlayhead != null) {{
          let badgeText = "";
          let badgeColor = "#22c55e";
          if (Math.abs(centsDiff) <= 15) {{
            badgeText = `0¢ In Tune`;
            badgeColor = "#22c55e";
            hudIntonation.textContent = `0¢ In Tune`;
            hudIntonation.className = "hud-value glow-green";
          }} else if (centsDiff > 15) {{
            badgeText = `+${{centsDiff}}¢ Sharp`;
            badgeColor = "#f59e0b";
            hudIntonation.textContent = `+${{centsDiff}}¢ Sharp`;
            hudIntonation.className = "hud-value glow-amber";
          }} else {{
            badgeText = `${{centsDiff}}¢ Flat`;
            badgeColor = "#06b6d4";
            hudIntonation.textContent = `${{centsDiff}}¢ Flat`;
            hudIntonation.className = "hud-value glow-cyan";
          }}

          // Floating badge next to playhead cursor
          const badgeW = 86;
          const badgeH = 20;
          ctx.beginPath();
          ctx.roundRect(PLAYHEAD_X + 16, cursorY - 10, badgeW, badgeH, 10);
          ctx.fillStyle = "rgba(18, 24, 36, 0.9)";
          ctx.fill();
          ctx.strokeStyle = badgeColor;
          ctx.lineWidth = 1.5;
          ctx.stroke();

          ctx.fillStyle = badgeColor;
          ctx.font = "bold 10px system-ui";
          ctx.textAlign = "center";
          ctx.textBaseline = "middle";
          ctx.fillText(badgeText, PLAYHEAD_X + 16 + badgeW / 2, cursorY);
        }}
        ctx.restore();
      }} else {{
        hudPitch.textContent = "-- (0 Hz)";
        hudIntonation.textContent = "--";
        hudIntonation.className = "hud-value";
      }}

      renderParticles();
      updateTeleprompter();
    }}

    /* =====================================================================
       SCORECARD MODAL & VOCAL RANGE PROFILE
       ==================================================================== */
    function openScorecard() {{
      const pct = totalScoredFrames > 0 ? Math.round((hitScoredFrames / totalScoredFrames) * 100) : 0;
      modalAccuracyScore.textContent = `${{pct}}%`;

      // Intonation bias
      const avgCents = intonationCentsCount > 0 ? (intonationCentsSum / intonationCentsCount).toFixed(1) : "0.0";
      let biasLabel = "Center";
      if (parseFloat(avgCents) > 5) biasLabel = "Slightly Sharp";
      else if (parseFloat(avgCents) < -5) biasLabel = "Slightly Flat";
      modalIntonationBias.textContent = `${{avgCents}}¢ (${{biasLabel}})`;

      // Vocal range
      const userRangeStr = sessionMinMidi != null && sessionMaxMidi != null
        ? `${{midiToBareNote(sessionMinMidi)}} to ${{midiToBareNote(sessionMaxMidi)}}`
        : "Sing more to profile";
      modalUserRange.textContent = userRangeStr;

      // Song range
      let songLowest = 127;
      let songHighest = 0;
      (currentChart.lines || []).forEach(l => {{
        (l.words || []).forEach(w => {{
          if (w.midi) {{
            songLowest = Math.min(songLowest, w.midi);
            songHighest = Math.max(songHighest, w.midi);
          }}
        }});
      }});
      modalSongRange.textContent = songLowest < songHighest
        ? `${{midiToBareNote(songLowest)}} to ${{midiToBareNote(songHighest)}}`
        : "--";

      // Recommended Key Shift
      let recShift = 0;
      if (sessionMinMidi != null && sessionMaxMidi != null && songLowest < songHighest) {{
        const userCenter = (sessionMinMidi + sessionMaxMidi) / 2.0;
        const songCenter = (songLowest + songHighest) / 2.0;
        recShift = Math.max(-6, Math.min(2, Math.round(userCenter - songCenter)));
      }}
      modalRecKey.textContent = recShift !== 0 ? `${{recShift > 0 ? '+' : ''}}${{recShift}} semitones` : "0 (Already optimal)";

      // Populate phrase breakdown
      modalPhraseList.innerHTML = "";
      let hardestPhraseIdx = null;
      let lowestAccuracy = 101;

      (currentChart.lines || []).forEach((line, idx) => {{
        const sc = phraseScores[idx] || {{ hits: 0, total: 0 }};
        const phrasePct = sc.total > 0 ? Math.round((sc.hits / sc.total) * 100) : 0;

        if (sc.total > 15 && phrasePct < lowestAccuracy) {{
          lowestAccuracy = phrasePct;
          hardestPhraseIdx = idx;
        }}

        const row = document.createElement("div");
        row.className = "phrase-item";
        row.innerHTML = `
          <span style="font-weight:600; min-width: 90px;">${{line.section || `Phrase ${{idx + 1}}`}}:</span>
          <span style="flex:1; color: var(--text-muted); overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">"${{line.fullLine}}"</span>
          <span style="font-weight:700; color:${{phrasePct >= 75 ? '#4ade80' : (phrasePct >= 50 ? '#fbbf24' : '#f43f5e')}}">${{phrasePct}}%</span>
          <button class="btn" style="padding: 2px 8px; font-size: 0.72rem;" onclick="practicePhrase(${{idx}})">🔁 Loop</button>
        `;
        modalPhraseList.appendChild(row);
      }});

      practiceHardestBtn.onclick = () => {{
        const targetIdx = hardestPhraseIdx != null ? hardestPhraseIdx : 0;
        practicePhrase(targetIdx);
      }};

      scorecardModal.classList.add("open");
    }}

    function closeScorecard() {{
      scorecardModal.classList.remove("open");
    }}

    window.practicePhrase = function(idx) {{
      const lines = currentChart.lines || [];
      const line = lines[idx];
      if (!line) return;
      const startT = Math.max(0, line.startTime - 0.2);
      const endT = line.words && line.words.length
        ? line.words[line.words.length - 1].start + line.words[line.words.length - 1].dur + 0.5
        : startT + 4.0;

      loopA = startT;
      loopB = endT;
      isLoopActive = true;
      loopSetABtn.textContent = `[A] ${{formatTime(loopA)}}`;
      loopSetBBtn.textContent = `[B] ${{formatTime(loopB)}}`;
      loopSetABtn.classList.add("btn-loop-active");
      loopSetBBtn.classList.add("btn-loop-active");
      updateLoopUI();

      closeScorecard();
      seekTo(loopA);
      if (!isPlaying) togglePlay();
    }};

    scorecardBtn.addEventListener("click", openScorecard);
    closeScorecardBtn.addEventListener("click", closeScorecard);
    singAgainBtn.addEventListener("click", () => {{
      closeScorecard();
      resetPlayhead();
      togglePlay();
    }});

    // Auto-fit Key Transposition
    autoFitKeyBtn.addEventListener("click", () => {{
      let songLowest = 127;
      let songHighest = 0;
      (currentChart.lines || []).forEach(l => {{
        (l.words || []).forEach(w => {{
          if (w.midi) {{
            songLowest = Math.min(songLowest, w.midi);
            songHighest = Math.max(songHighest, w.midi);
          }}
        }});
      }});
      if (sessionMinMidi != null && sessionMaxMidi != null && songLowest < songHighest) {{
        const userCenter = (sessionMinMidi + sessionMaxMidi) / 2.0;
        const songCenter = (songLowest + songHighest) / 2.0;
        const rec = Math.max(-6, Math.min(2, Math.round(userCenter - songCenter)));
        transposeShift = rec;
        updateTransposeUI();
        alert(`Transposed song by ${{rec > 0 ? '+' : ''}}${{rec}} semitones to fit your range (${{midiToBareNote(sessionMinMidi)}} - ${{midiToBareNote(sessionMaxMidi)}})!`);
      }} else {{
        alert("Sing a phrase first so we can analyze your natural vocal range!");
      }}
    }});

    /* =====================================================================
       EVENT LISTENERS & BINDINGS
       ===================================================================== */
    playPauseBtn.addEventListener("click", togglePlay);
    restartBtn.addEventListener("click", resetPlayhead);
    micBtn.addEventListener("click", toggleMicrophone);

    skipIntroBtn.addEventListener("click", () => {{
      const lines = currentChart.lines || [];
      const firstStart = lines.length > 0 ? (lines[0].startTime || 0) : 0;
      seekTo(Math.max(0, firstStart - 1.5));
      if (!isPlaying) togglePlay();
    }});

    timeScrubber.addEventListener("input", (e) => {{
      seekTo(parseFloat(e.target.value));
    }});

    sectionSelect.addEventListener("change", (e) => {{
      seekTo(parseFloat(e.target.value));
    }});

    window.addEventListener("keydown", (e) => {{
      if (e.code === "Space" && e.target.tagName !== "INPUT") {{
        e.preventDefault();
        togglePlay();
      }}
    }});

    // Preset selector (Song vs Warm-Ups)
    presetSelect.addEventListener("change", (e) => {{
      const val = e.target.value;
      if (val === "song") {{
        loadChartData(DEFAULT_CHART);
        backingAudio.removeAttribute("src");
        vocalsAudio.removeAttribute("src");
      }} else if (WARMUP_CHARTS[val]) {{
        loadChartData(WARMUP_CHARTS[val]);
        // Warm-ups use internal synth or optional backing
        backingAudio.removeAttribute("src");
        vocalsAudio.removeAttribute("src");
        guideSynthEnabled = true;
        synthToggleBtn.textContent = "🎹 Guide Synth: ON";
        synthToggleBtn.classList.add("btn-toggle-active");
      }}
    }});

    // Transposition
    transposeDownBtn.addEventListener("click", () => {{
      if (transposeShift > -6) {{
        transposeShift--;
        updateTransposeUI();
      }}
    }});

    transposeUpBtn.addEventListener("click", () => {{
      if (transposeShift < 2) {{
        transposeShift++;
        updateTransposeUI();
      }}
    }});

    function updateTransposeUI() {{
      transposeDisplay.textContent = transposeShift > 0 ? `+${{transposeShift}}` : `${{transposeShift}}`;
      hudKey.textContent = `${{transposeDisplay.textContent}} st`;
    }}

    // Scroll Speed Cycle
    scrollSpeedBtn.addEventListener("click", () => {{
      scrollSpeedIndex = (scrollSpeedIndex + 1) % SCROLL_SPEEDS.length;
      pixelsPerSecond = SCROLL_SPEEDS[scrollSpeedIndex].pps;
      scrollSpeedBtn.textContent = SCROLL_SPEEDS[scrollSpeedIndex].label;
    }});

    // Audio Sync Offset Calibration
    syncMinusBtn.addEventListener("click", () => {{
      syncOffsetSec = Math.max(-0.5, syncOffsetSec - 0.05);
      updateSyncOffsetUI();
    }});

    syncPlusBtn.addEventListener("click", () => {{
      syncOffsetSec = Math.min(0.5, syncOffsetSec + 0.05);
      updateSyncOffsetUI();
    }});

    function updateSyncOffsetUI() {{
      const ms = Math.round(syncOffsetSec * 1000);
      syncOffsetDisplay.textContent = ms > 0 ? `+${{ms}}ms` : `${{ms}}ms`;
    }}

    // Guide Synth Toggle
    synthToggleBtn.addEventListener("click", () => {{
      initAudioContext();
      guideSynthEnabled = !guideSynthEnabled;
      synthToggleBtn.textContent = guideSynthEnabled ? "🎹 Guide Synth: ON" : "🎹 Guide Synth: OFF";
      synthToggleBtn.classList.toggle("btn-toggle-active", guideSynthEnabled);
      if (!guideSynthEnabled) updateGuideSynth(null);
    }});

    // Speed Toggle (100% / 75%)
    speedToggleBtn.addEventListener("click", () => {{
      if (playbackSpeed === 1.0) {{
        playbackSpeed = 0.75;
      }} else {{
        playbackSpeed = 1.0;
      }}
      speedToggleBtn.textContent = `⚡ ${{Math.round(playbackSpeed * 100)}}%`;
      syncStemPlayback();
    }});

    // Chart File Input
    chartFileInput.addEventListener("change", (e) => {{
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = (event) => {{
        try {{
          const parsed = JSON.parse(event.target.result);
          loadChartData(parsed);
        }} catch (err) {{
          alert("Error parsing JSON chart: " + err.message);
        }}
      }};
      reader.readAsText(file);
    }});

    // Vocals Stem File Input
    vocalsFileInput.addEventListener("change", (e) => {{
      const file = e.target.files[0];
      if (!file) return;
      vocalsAudio.src = URL.createObjectURL(file);
      vocalsAudio.load();
    }});

    // Backing Stem File Input
    backingFileInput.addEventListener("change", (e) => {{
      const file = e.target.files[0];
      if (!file) return;
      backingAudio.src = URL.createObjectURL(file);
      backingAudio.load();
    }});

    /* =====================================================================
       INITIALIZATION
       ===================================================================== */
    window.addEventListener("DOMContentLoaded", () => {{
      resizeCanvas();
      loadChartData(DEFAULT_CHART);
      updateStemVolume();
      requestAnimationFrame(render);
    }});
  </script>
</body>
</html>
"""

with open("vocal-highway.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated vocal-highway.html successfully ({len(html_content)} bytes).")
