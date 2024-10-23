
import pytest
from paranoid_devdroid.plugins.core.hallucination_detection import HallucinationDetection

def test_monitor_output_normal():
    detector = HallucinationDetection()
    result = detector.monitor_output(1, "This is a normal output.")
    assert "seems normal" in result
    assert len(detector.get_flagged_outputs()) == 0

def test_monitor_output_hallucination():
    detector = HallucinationDetection()
    result = detector.monitor_output(2, "Gibberish gibberish gibberish gibberish gibberish")
    assert "flagged for potential hallucination" in result
    assert len(detector.get_flagged_outputs()) == 1
