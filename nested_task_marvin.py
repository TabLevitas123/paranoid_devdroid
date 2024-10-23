
class NestedTaskMarvin(MultiStageMarvin):
    def __init__(self, name, task_complexity, accuracy_level=3, max_resources=5, learning_rate=0.1, discount_factor=0.95, epsilon=1.0):
        super().__init__(name, task_complexity, accuracy_level, max_resources, learning_rate, discount_factor, epsilon)
        self.dependencies = {}

    def add_dependency(self, task_name, dependent_task):
        if task_name not in self.dependencies:
            self.dependencies[task_name] = []
        self.dependencies[task_name].append(dependent_task)

    def check_dependencies(self, task_name):
        if task_name not in self.dependencies:
            return True
        for dep_task in self.dependencies[task_name]:
            if not dep_task["completed"]:
                return False
        return True

    def complete_task(self, task_name):
        task_duration = super().complete_task() or 0.0
        if task_name in self.dependencies:
            self.dependencies[task_name] = [{"name": dep["name"], "completed": True} for dep in self.dependencies[task_name]]

    def handle_nested_tasks(self, task_name):
        if self.check_dependencies(task_name):
            self.optimize_task_with_name(task_name)
            self.complete_task(task_name)

    def optimize_task_with_name(self, task_name):
        action = self.choose_action()
        self.take_action_with_name(action, task_name)
