
import pytest
from paranoid_devdroid.plugins.core.inter_agent_communication import InterAgentCommunication

def test_send_message():
    communication = InterAgentCommunication()
    message = communication.send_message(1, 2, "Test Message")
    assert "Message from Agent 1 to Agent 2: Test Message" in message
    assert len(communication.get_communication_log()) == 1
