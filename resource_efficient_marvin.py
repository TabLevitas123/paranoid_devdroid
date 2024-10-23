
class ResourceEfficientMarvin(PerformanceTrackingMarvin):
    def __init__(self, name, task_complexity, accuracy_level=3, max_resources=5, learning_rate=0.1, discount_factor=0.95):
        super().__init__(name, task_complexity, accuracy_level, learning_rate, discount_factor)
        self.available_resources = max_resources

    def create_sub_agent(self):
        if self.available_resources > 0:
            super().create_sub_agent()
            self.available_resources -= 1
        else:
            print(f"{self.name} cannot create sub-agents due to insufficient resources.")

    def complete_task(self):
        task_duration = super().complete_task()
        self.available_resources += 1
        return task_duration
