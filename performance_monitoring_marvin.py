
class PerformanceMonitoringMarvin(NestedTaskMarvin):
    def __init__(self, name, task_complexity, accuracy_level=3, max_resources=5, learning_rate=0.1, discount_factor=0.95, epsilon=1.0):
        super().__init__(name, task_complexity, accuracy_level, max_resources, learning_rate, discount_factor, epsilon)
        self.success_count = 0
        self.failure_count = 0
        self.resource_usage_over_time = []
        self.task_results = []

    def track_resource_usage(self):
        self.resource_usage_over_time.append(self.available_resources)

    def log_task_result(self, task_name, success=True, failure_reason=None):
        if success:
            self.success_count += 1
        else:
            self.failure_count += 1

    def complete_task(self, task_name):
        try:
            super().complete_task(task_name)
            self.log_task_result(task_name, success=True)
        except Exception as e:
            self.log_task_result(task_name, success=False, failure_reason=str(e))

    def monitor_performance(self):
        self.track_resource_usage()
        self.log_event(event_type="Performance Monitoring", details=f"Tasks completed: {self.success_count}, Failures: {self.failure_count}.")
