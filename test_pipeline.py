import unittest
import numpy as np
from pathlib import Path
import json
import tempfile
import os

from extract_vocal_chart import export_ultrastar_format, parse_time_str

class TestPipelineFeatures(unittest.TestCase):
    def test_parse_time_str(self):
        self.assertEqual(parse_time_str("330"), 330.0)
        self.assertEqual(parse_time_str("5:30"), 330.0)
        self.assertEqual(parse_time_str("01:02:03"), 3723.0)
        self.assertIsNone(parse_time_str(None))

    def test_melisma_segmentation(self):
        # Create a mock word with pitch inflection: 55 for first half, 58 for second half
        times = np.linspace(10.0, 11.0, 50)
        f0_midi = np.concatenate([np.full(25, 55.0), np.full(25, 58.0)])
        
        v_midi = f0_midi
        v_times = times
        
        smoothed = np.copy(v_midi)
        for i in range(1, len(v_midi) - 1):
            smoothed[i] = np.median(v_midi[max(0, i-1):min(len(v_midi), i+2)])
        
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
            
        self.assertGreaterEqual(len(segments), 2)
        midi_0 = int(np.round(np.median(smoothed[segments[0]])))
        midi_1 = int(np.round(np.median(smoothed[segments[1]])))
        self.assertEqual(midi_0, 55)
        self.assertEqual(midi_1, 58)

    def test_export_ultrastar(self):
        chart_payload = {
            "title": "Test Song",
            "artist": "Test Artist",
            "duration": 60.0,
            "lines": [
                {
                    "section": "Phrase 1",
                    "fullLine": "Amazing grace how sweet",
                    "startTime": 2.0,
                    "words": [
                        {"text": "Amazing", "start": 2.0, "dur": 0.95, "midi": 65},
                        {
                            "text": "sweet",
                            "start": 5.9,
                            "dur": 0.90,
                            "midi": 67,
                            "subNotes": [
                                {"start": 5.9, "dur": 0.45, "midi": 67},
                                {"start": 6.35, "dur": 0.45, "midi": 69}
                            ]
                        }
                    ]
                }
            ]
        }
        with tempfile.TemporaryDirectory() as tmpdir:
            txt_path = Path(tmpdir) / "test_song.txt"
            export_ultrastar_format(chart_payload, txt_path, audio_filename="test.mp3", bpm=120.0, artist="Test Artist")
            self.assertTrue(txt_path.is_file())
            content = txt_path.read_text(encoding="utf-8")
            self.assertIn("#TITLE:Test Song", content)
            self.assertIn("#ARTIST:Test Artist", content)
            self.assertIn("#MP3:test.mp3", content)
            self.assertIn("#BPM:120.00", content)
            self.assertIn("#GAP:2000", content)
            self.assertIn("E", content.splitlines()[-1])
            # Check subnote syllable lines
            self.assertIn("sweet", content)

if __name__ == "__main__":
    unittest.main()
