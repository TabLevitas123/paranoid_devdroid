
import random

class Agent:
    def __init__(self, name, task):
        self.name = name
        self.task = task
        self.sub_agents = []
        self.is_active = True

    def create_sub_agent(self, sub_agent_name, sub_agent_task):
        # Create and append sub-agents to the agent's task list
        sub_agent = Agent(sub_agent_name, sub_agent_task)
        self.sub_agents.append(sub_agent)
        return sub_agent

    def communicate(self, message):
        # Extend this communication logic to inter-agent communication protocols later
        print(f"{self.name} says: {message}")

    def report(self):
        # Provide a detailed report of the agent and sub-agent tasks
        print(f"Agent: {self.name} is handling task: {self.task}")
        for sub_agent in self.sub_agents:
            sub_agent.report()

class HallucinationMonitor(Agent):
    def __init__(self, name, task, hallucination_threshold=0.1):
        super().__init__(name, task)
        self.hallucination_threshold = hallucination_threshold

    def detect_hallucination(self, agent_decision):
        # Check whether the agent decision crosses the hallucination threshold
        if random.random() > self.hallucination_threshold:
            print(f"Agent {self.name} detected a hallucination in decision: {agent_decision}")
            return True
        return False

# Additional refactoring for other components can follow
