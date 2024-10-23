
class AgentPrompting:
    def __init__(self):
        self.active_agents = []

    def create_agent(self, task):
        agent = {
            "id": len(self.active_agents) + 1,
            "task": task,
            "status": "pending"
        }
        self.active_agents.append(agent)
        return agent

    def get_active_agents(self):
        return self.active_agents

    def complete_agent_task(self, agent_id):
        for agent in self.active_agents:
            if agent["id"] == agent_id:
                agent["status"] = "complete"
                return f"Agent {agent_id} completed its task."
        return "Agent not found."

# Example Usage
if __name__ == "__main__":
    agent_prompting = AgentPrompting()
    agent1 = agent_prompting.create_agent("Analyze Data")
    agent2 = agent_prompting.create_agent("Write Report")
    print(agent_prompting.get_active_agents())
    print(agent_prompting.complete_agent_task(agent1["id"]))
