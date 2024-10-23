
import random

class Agent:
    def __init__(self, name, task):
        self.name = name
        self.task = task
        self.sub_agents = []
        self.is_active = True

    def create_sub_agent(self, sub_agent_name, sub_agent_task):
        sub_agent = Agent(sub_agent_name, sub_agent_task)
        self.sub_agents.append(sub_agent)
        return sub_agent

    def communicate(self, message):
        # Basic communication logic (expand this later for inter-agent communication)
        print(f"{self.name} says: {message}")

    def report(self):
        # Basic report for the agent and its sub-agents
        print(f"Agent: {self.name} is handling task: {self.task}")
        for sub_agent in self.sub_agents:
            sub_agent.report()

class HallucinationMonitor(Agent):
    def __init__(self, name, task, hallucination_threshold=0.1):
        super().__init__(name, task)
        self.hallucination_threshold = hallucination_threshold

    def detect_hallucination(self, agent_decision):
        # Basic logic to detect hallucinations (randomly decide for now, could improve with ML later)
        hallucination_score = random.random()
        if hallucination_score > self.hallucination_threshold:
            self.communicate("Warning! Potential hallucination detected.")
            return True
        else:
            self.communicate("All clear. No hallucinations detected.")
            return False
