
class AdaptiveLearningMarvin(PredictiveOptimizationMarvin):
    def __init__(self, name, task_complexity, accuracy_level=3, max_resources=5, learning_rate=0.1, discount_factor=0.95, epsilon=1.0):
        super().__init__(name, task_complexity, accuracy_level, max_resources, learning_rate, discount_factor, epsilon)
        self.task_outcome_history = []

    def learn_from_task_outcomes(self):
        success_rate = self.success_count / (self.success_count + self.failure_count) if (self.success_count + self.failure_count) > 0 else 1.0
        if success_rate < 0.7:
            self.learning_rate *= 1.05
        else:
            self.learning_rate *= 0.95

    def adjust_decision_making(self):
        if self.failure_count > self.success_count:
            self.log_event(event_type="Decision Adjustment", details="Shifting focus to simpler tasks.")
        elif self.success_count > self.failure_count:
            self.log_event(event_type="Decision Adjustment", details="Focusing on larger tasks.")

    def complete_task(self, task_name):
        super().complete_task(task_name)
        self.task_outcome_history.append({"task": task_name, "result": "success" if self.success_count else "failure"})
        self.learn_from_task_outcomes()
        self.adjust_decision_making()
    