
class PerformanceMonitoringMarvin(NestedTaskMarvin):
    def __init__(self, name, task_complexity, accuracy_level=3, max_resources=5, learning_rate=0.1, discount_factor=0.95, epsilon=1.0):
        super().__init__(name, task_complexity, accuracy_level, max_resources, learning_rate, discount_factor, epsilon)
        self.success_count = 0
        self.failure_count = 0
        self.resource_usage_over_time = []
        self.task_results = []
        self.performance_threshold = 0.75  # Threshold for performance adjustments

    def track_resource_usage(self):
        self.resource_usage_over_time.append(self.max_resources)
        print(f"Tracking resource usage: {self.max_resources}")
    
    def analyze_task_performance(self, task_result):
        if task_result == 'success':
            self.success_count += 1
        else:
            self.failure_count += 1

        self.task_results.append(task_result)
        success_rate = self.success_count / (self.success_count + self.failure_count)
        
        # Adjust resources dynamically based on success rate
        if success_rate < self.performance_threshold:
            self.max_resources += 1
            print(f"Performance below threshold, increasing resources to {self.max_resources}")
        else:
            self.max_resources = max(1, self.max_resources - 1)
            print(f"Performance above threshold, decreasing resources to {self.max_resources}")

    def monitor_overall_performance(self):
        success_rate = self.success_count / (self.success_count + self.failure_count)
        print(f"Overall success rate: {success_rate:.2f}")
        return success_rate
