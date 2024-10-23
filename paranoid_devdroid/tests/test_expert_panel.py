
import pytest
from paranoid_devdroid.plugins.core.expert_panel import ExpertPanel

def test_add_expert():
    panel = ExpertPanel()
    panel.add_expert("Dr. Smith", "AI Ethics")
    assert len(panel.experts) == 1
    assert panel.experts["Dr. Smith"] == "AI Ethics"

def test_deliberate():
    panel = ExpertPanel()
    panel.add_expert("Dr. Smith", "AI Ethics")
    response = panel.deliberate("How should AI handle privacy?")
    assert "Dr. Smith" in response
    assert "AI Ethics" in response["Dr. Smith"]
