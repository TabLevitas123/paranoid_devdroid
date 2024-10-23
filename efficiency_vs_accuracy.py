
class MarvinAgentWithAccuracy:
    def __init__(self, name, task_complexity, accuracy_level=3):
        self.name = name
        self.task_complexity = task_complexity
        self.sub_agents = []
        self.accuracy_level = accuracy_level  # Default is level 3 (moderate balance between efficiency and accuracy)
    
    def assess_task(self):
        if self.task_complexity > 5:
            print(f"{self.name} says: Task too complex, need sub-agents!")
            self.create_sub_agents(self.task_complexity // 5)
        else:
            print(f"{self.name} can handle the task without sub-agents!")

    def create_sub_agents(self, num_sub_agents):
        for i in range(num_sub_agents):
            sub_agent = MarvinAgentWithAccuracy(
                name=f"Sub-Agent-{i + 1}", 
                task_complexity=self.task_complexity / (i + 1), 
                accuracy_level=self.accuracy_level
            )
            self.sub_agents.append(sub_agent)
            print(f"{self.name} created {sub_agent.name} for task delegation.")

    def execute_task(self):
        if self.accuracy_level == 1:
            print(f"{self.name} is executing the task with max efficiency (minimal verification).")
        elif self.accuracy_level == 5:
            print(f"{self.name} is executing the task with max accuracy (extensive verification and monitoring).")
        
        if self.sub_agents:
            for sub_agent in self.sub_agents:
                sub_agent.execute_task()
        else:
            print(f"{self.name} is executing the task solo!")
