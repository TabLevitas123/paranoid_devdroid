
class MetaLearningMarvin(AdaptiveLearningMarvin):
    def __init__(self, name, task_complexity, accuracy_level=3, max_resources=5, learning_rate=0.1, discount_factor=0.95, epsilon=1.0):
        super().__init__(name, task_complexity, accuracy_level, max_resources, learning_rate, discount_factor, epsilon)
        self.meta_learning_rate = 0.05

    def self_diagnostics(self):
        total_tasks = self.success_count + self.failure_count
        success_rate = self.success_count / total_tasks if total_tasks > 0 else 1.0
        self.adjust_learning_strategy(success_rate)

    def adjust_learning_strategy(self, success_rate):
        if success_rate < 0.6:
            self.meta_learning_rate *= 1.1
            self.learning_rate *= 1.05
        elif success_rate > 0.8:
            self.meta_learning_rate *= 0.9
            self.learning_rate *= 0.95

    def meta_learn(self):
        self.self_diagnostics()
        self.log_event(event_type="Meta-Learning", details="Meta-learning applied to refine Marvin's learning processes.")
    