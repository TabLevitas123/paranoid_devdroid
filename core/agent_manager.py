
# AgentManager: Handles agent creation, task assignment, and communication

class Agent:
    def __init__(self, name):
        self.name = name
        self.memory = []
        self.tasks = []
    
    def add_memory(self, memory):
        self.memory.append(memory)
    
    def assign_task(self, task):
        self.tasks.append(task)
        print(f"Task {task} assigned to agent {self.name}")

class AgentManager:
    def __init__(self):
        self.agents = []

    def spawn_agent(self, name):
        agent = Agent(name)
        self.agents.append(agent)
        print(f"Agent {name} spawned.")
        return agent

    def assign_task(self, agent, task):
        agent.assign_task(task)

    def communicate(self, agent_from, agent_to, message):
        # Simple communication function
        print(f"Message from {agent_from.name} to {agent_to.name}: {message}")
        agent_to.add_memory(message)

if __name__ == "__main__":
    # Example usage of AgentManager
    manager = AgentManager()
    agent1 = manager.spawn_agent("Marvin")
    agent2 = manager.spawn_agent("Hal")
    
    manager.assign_task(agent1, "Solve complex equation")
    manager.communicate(agent1, agent2, "I have solved the equation.")
