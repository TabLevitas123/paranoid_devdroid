
from agent_base import Agent, HallucinationMonitor
from roastmaster import Roastmaster
from verification_agent import VerificationAgent
from expert_panel import ExpertPanel, Expert
from communication_protocol import CommunicationProtocol
import logging

class Marvin(Agent):
    def __init__(self, name, task, efficiency_level=3):
        super().__init__(name, task)
        self.efficiency_level = efficiency_level
        self.communication_protocol = CommunicationProtocol()
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.DEBUG)
        self.orchestrated_tasks = []

        # Create agents based on efficiency level
        self.verification_agent = VerificationAgent(self.name, "verification task")
        self.roastmaster = Roastmaster(self.name, "roast management")
        self.expert_panel = ExpertPanel()

    def allocate_task(self, agent, task):
        try:
            agent.task = task
            self.logger.info(f"Task '{task}' allocated to agent {agent.name}.")
            self.orchestrated_tasks.append((agent.name, task))
        except Exception as e:
            self.logger.error(f"Error allocating task '{task}' to agent {agent.name}: {str(e)}")

    def communicate_task_updates(self):
        for agent_name, task in self.orchestrated_tasks:
            message = f"Task update: {task} for agent {agent_name}."
            self.communication_protocol.send_message(agent_name, message)
            self.logger.info(f"Communicated task update for agent {agent_name}: {message}")

    def monitor_performance(self):
        # Log performance monitoring and ensure tasks are executed correctly
        for agent in [self.verification_agent, self.roastmaster]:
            self.logger.info(f"Monitoring performance of {agent.name}.")
            agent.perform_task()

        self.expert_panel.evaluate_agents([self.verification_agent, self.roastmaster])

