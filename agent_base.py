
import random
import logging

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
        self.hallucination_count = 0
        self.log = []

    def detect_hallucination(self, task_outcome):
        # Anomaly detection based on a random threshold (can be enhanced further)
        if random.random() < self.hallucination_threshold:
            self.hallucination_count += 1
            self.log_hallucination(task_outcome)
            self.correct_hallucination()
            return True
        return False

    def log_hallucination(self, task_outcome):
        # Log the hallucination details with severity levels
        severity = "Critical" if self.hallucination_count > 3 else "Minor"
        log_entry = {
            "agent": self.name,
            "task": self.task,
            "outcome": task_outcome,
            "severity": severity,
            "hallucination_count": self.hallucination_count
        }
        self.log.append(log_entry)
        logging.info(f"Hallucination detected: {log_entry}")

    def correct_hallucination(self):
        # Corrective mechanism: Reassess or seek external validation
        print(f"{self.name} is correcting hallucination...")
        self.task = "Re-evaluated task after hallucination"

# Example usage
if __name__ == "__main__":
    monitor = HallucinationMonitor(name="Hallucination Monitor", task="Monitor for hallucinations")
    for _ in range(10):
        monitor.detect_hallucination("Task outcome XYZ")
