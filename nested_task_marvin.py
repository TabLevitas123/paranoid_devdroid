
class NestedTaskMarvin(MultiStageMarvin):
    def __init__(self, name, task_complexity, accuracy_level=3, max_resources=5, learning_rate=0.1, discount_factor=0.95, epsilon=1.0):
        super().__init__(name, task_complexity, accuracy_level, max_resources, learning_rate, discount_factor, epsilon)
        self.dependencies = {}
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.DEBUG)

    def add_dependency(self, task_name, dependent_task):
        if task_name not in self.dependencies:
            self.dependencies[task_name] = []
        self.dependencies[task_name].append(dependent_task)
        self.logger.info(f"Dependency added: {task_name} depends on {dependent_task}")

    def execute_nested_tasks(self):
        # Execute tasks in the order of dependencies
        for task, dependents in self.dependencies.items():
            self.logger.info(f"Executing task: {task}")
            for dependent in dependents:
                self.logger.info(f"Executing dependent task: {dependent}")
                # Simulate task execution
                self.execute_task(dependent)

    def execute_task(self, task_name):
        self.logger.info(f"Task {task_name} executed.")
    
    def prioritize_nested_tasks(self):
        # Prioritize tasks based on complexity and dependencies
        sorted_tasks = sorted(self.dependencies.items(), key=lambda x: len(x[1]), reverse=True)
        for task, dependents in sorted_tasks:
            self.logger.info(f"Prioritizing task: {task} with {len(dependents)} dependents.")
