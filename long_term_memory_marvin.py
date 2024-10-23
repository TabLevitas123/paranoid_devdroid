
class LongTermMemoryMarvin(AutonomousSchedulingMarvin):
    def __init__(self, name, task_complexity, accuracy_level=3, max_resources=5, learning_rate=0.1, discount_factor=0.95, epsilon=1.0):
        super().__init__(name, task_complexity, accuracy_level, max_resources, learning_rate, discount_factor, epsilon)
        self.long_term_memory = []
        self.memory_limit = 1000  # Limit on how many memory entries can be stored
        self.memory_cleanup_threshold = 0.8  # When memory exceeds 80%, initiate cleanup

    def store_memory(self, task_name, task_result, strategies_used, resources_used):
        memory_entry = {
            "task_name": task_name,
            "task_result": task_result,
            "strategies_used": strategies_used,
            "resources_used": resources_used
        }
        self.long_term_memory.append(memory_entry)
        print(f"Memory stored for task: {task_name}")

        # Check if memory exceeds the cleanup threshold
        if len(self.long_term_memory) > self.memory_limit * self.memory_cleanup_threshold:
            self.cleanup_memory()

    def retrieve_memory(self, task_name):
        for memory in self.long_term_memory:
            if memory["task_name"] == task_name:
                print(f"Memory retrieved for task: {task_name}")
                return memory
        print(f"No memory found for task: {task_name}")
        return None

    def cleanup_memory(self):
        # Keep only the most recent 80% of memory entries
        cutoff = int(self.memory_limit * self.memory_cleanup_threshold)
        self.long_term_memory = self.long_term_memory[-cutoff:]
        print("Memory cleanup performed, retaining most recent entries.")
