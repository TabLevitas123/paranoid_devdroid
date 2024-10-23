
class CollaborativeMarvin(MultiAgentMarvin):
    def __init__(self, name, task_complexity, accuracy_level=3, max_resources=5, learning_rate=0.1, discount_factor=0.95, epsilon=1.0):
        super().__init__(name, task_complexity, accuracy_level, max_resources, learning_rate, discount_factor, epsilon)
        self.sub_agent_communications = []

    def coordinate_sub_agents(self, task_name, sub_agents):
        self.log_event(event_type="Coordination", details=f"Coordinating sub-agents {sub_agents} on task '{task_name}'.")
        for agent in sub_agents:
            self.assign_sub_task(agent, task_name)

    def communicate_between_agents(self, sender, receiver, message):
        communication_log = {"from": sender, "to": receiver, "message": message}
        self.sub_agent_communications.append(communication_log)

    def resolve_dependencies(self, tasks):
        sorted_tasks = sorted(tasks, key=lambda t: t["dependency"])
        return sorted_tasks
    