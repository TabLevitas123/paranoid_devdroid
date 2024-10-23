
class GoalOrientedMarvin(MetaLearningMarvin):
    def __init__(self, name, task_complexity, accuracy_level=3, max_resources=5, learning_rate=0.1, discount_factor=0.95, epsilon=1.0):
        super().__init__(name, task_complexity, accuracy_level, max_resources, learning_rate, discount_factor, epsilon)
        self.goals = []
        self.completed_goals = []

    def set_goal(self, goal_name, priority):
        goal = {"name": goal_name, "priority": priority, "completed": False}
        self.goals.append(goal)

    def prioritize_goals(self):
        self.goals.sort(key=lambda g: g["priority"], reverse=True)

    def execute_goal(self):
        if not self.goals:
            return
        self.prioritize_goals()
        highest_priority_goal = self.goals[0]
        task_name = f"Task for {highest_priority_goal['name']}"
        self.handle_nested_tasks(task_name)
        highest_priority_goal["completed"] = True
        self.completed_goals.append(highest_priority_goal)
        self.goals.remove(highest_priority_goal)

    def review_goals(self):
        self.log_event(event_type="Goals Review", details=f"Completed goals: {self.completed_goals}.")
    