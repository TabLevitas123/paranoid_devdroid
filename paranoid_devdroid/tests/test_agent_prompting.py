
import pytest
from paranoid_devdroid.plugins.core.agent_prompting import AgentPrompting

def test_create_agent():
    agent_prompting = AgentPrompting()
    agent = agent_prompting.create_agent("Test Task")
    assert agent["task"] == "Test Task"
    assert agent["status"] == "pending"
    assert len(agent_prompting.get_active_agents()) == 1

def test_complete_agent_task():
    agent_prompting = AgentPrompting()
    agent = agent_prompting.create_agent("Test Task")
    response = agent_prompting.complete_agent_task(agent["id"])
    assert response == f"Agent {agent['id']} completed its task."
    assert agent["status"] == "complete"
