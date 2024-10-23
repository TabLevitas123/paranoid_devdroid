
class GoalOrientedMarvin(MetaLearningMarvin):
    def __init__(self, name, task_complexity, accuracy_level=3, max_resources=5, learning_rate=0.1, discount_factor=0.95, epsilon=1.0):
        super().__init__(name, task_complexity, accuracy_level, max_resources, learning_rate, discount_factor, epsilon)
        self.goals = []
        self.completed_goals = []
        self.dynamic_priority_threshold = 0.6  # Adjust goal priorities based on task outcomes
    
    def set_goal(self, goal_name, priority):
        goal = {"name": goal_name, "priority": priority, "completed": False}
        self.goals.append(goal)
        print(f"Goal set: {goal_name} with priority {priority}")

    def complete_goal(self, goal_name):
        for goal in self.goals:
            if goal["name"] == goal_name and not goal["completed"]:
                goal["completed"] = True
                self.completed_goals.append(goal)
                print(f"Goal completed: {goal_name}")
                self.adjust_goal_priorities()
                break
    
    def adjust_goal_priorities(self):
        # Adjust priorities based on completed goals and task performance
        success_rate = self.success_count / (self.success_count + self.failure_count) if (self.success_count + self.failure_count) > 0 else 0
        for goal in self.goals:
            if not goal["completed"]:
                if success_rate < self.dynamic_priority_threshold:
                    goal["priority"] += 1  # Increase priority for harder tasks
                else:
                    goal["priority"] = max(1, goal["priority"] - 1)  # Decrease priority for easier tasks
        print("Goal priorities adjusted based on performance.")

    def prioritize_goals(self):
        # Sort goals based on priority
        self.goals.sort(key=lambda x: x['priority'], reverse=True)
        print(f"Goals prioritized: {[goal['name'] for goal in self.goals]}")
