
class AdaptiveLearningMarvin(PredictiveOptimizationMarvin):
    def __init__(self, name, task_complexity, accuracy_level=3, max_resources=5, learning_rate=0.1, discount_factor=0.95, epsilon=1.0):
        super().__init__(name, task_complexity, accuracy_level, max_resources, learning_rate, discount_factor, epsilon)
        self.task_outcome_history = []
        self.dynamic_adjustment_factor = 0.05  # New dynamic factor for adjustment
    
    def learn_from_task_outcomes(self):
        success_rate = self.success_count / (self.success_count + self.failure_count) if (self.success_count + self.failure_count) > 0 else 0
        # Dynamic adjustment of learning rate and resource allocation based on outcomes
        if success_rate < 0.5:
            self.learning_rate += self.dynamic_adjustment_factor  # Increase learning rate if success rate is low
            self.max_resources += 1  # Allocate more resources if success is low
        else:
            self.learning_rate -= self.dynamic_adjustment_factor  # Decrease learning rate if success rate is high
            self.max_resources = max(1, self.max_resources - 1)  # Reduce resources if success is high
        self.task_outcome_history.append(success_rate)
    
    def optimize_performance(self):
        # Improved performance tracking and adjustment
        if len(self.task_outcome_history) > 10:
            recent_outcomes = self.task_outcome_history[-10:]
            avg_success_rate = sum(recent_outcomes) / len(recent_outcomes)
            if avg_success_rate < 0.6:
                self.learning_rate += self.dynamic_adjustment_factor  # More aggressive adjustments for long-term performance
                print(f"Adjusting learning rate to {self.learning_rate} based on long-term performance")
            else:
                print("Performance is optimal, no adjustments needed.")
