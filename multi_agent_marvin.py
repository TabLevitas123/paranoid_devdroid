
class MultiAgentMarvin(RealTimeAwarenessMarvin):
    def __init__(self, name, task_complexity, accuracy_level=3, max_resources=5, learning_rate=0.1, discount_factor=0.95, epsilon=1.0):
        super().__init__(name, task_complexity, accuracy_level, max_resources, learning_rate, discount_factor, epsilon)
        self.sub_agents = []
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.DEBUG)

    def create_sub_agent(self, agent_name):
        if self.available_resources > 0:
            sub_agent = {"name": agent_name, "status": "active", "tasks": []}
            self.sub_agents.append(sub_agent)
            self.available_resources -= 1
            self.logger.info(f"Sub-agent {agent_name} created successfully.")
        else:
            self.logger.warning(f"Failed to create sub-agent {agent_name}: No available resources.")

    def delegate_task(self, agent_name, task):
        for agent in self.sub_agents:
            if agent["name"] == agent_name and agent["status"] == "active":
                agent["tasks"].append(task)
                self.logger.info(f"Task {task} delegated to sub-agent {agent_name}.")
                break
    
    def synchronize_agents(self):
        for agent in self.sub_agents:
            if agent["status"] == "active":
                self.logger.info(f"Synchronizing tasks for {agent['name']}. Tasks: {agent['tasks']}")

    def reallocate_resources(self):
        # Dynamically reallocate resources based on task load
        for agent in self.sub_agents:
            if len(agent["tasks"]) > 2:
                self.logger.info(f"Reallocating additional resources to {agent['name']} based on task load.")
                self.max_resources += 1
            elif len(agent["tasks"]) == 0:
                self.logger.info(f"Decreasing resources for {agent['name']} due to idle status.")
                self.max_resources = max(1, self.max_resources - 1)
