
class DynamicExplorationMarvin(ResourceEfficientMarvin):
    def __init__(self, name, task_complexity, accuracy_level=3, max_resources=5, learning_rate=0.1, discount_factor=0.95, epsilon=1.0, min_epsilon=0.1, decay_rate=0.99):
        super().__init__(name, task_complexity, accuracy_level, max_resources, learning_rate, discount_factor)
        self.epsilon = epsilon

    def choose_action(self):
        if np.random.rand() < self.epsilon:
            action = np.random.choice(["create_sub_agent", "execute_solo"])
        else:
            best_action = np.argmax(self.q_table[self.state[0]])
            action = "create_sub_agent" if best_action == 0 else "execute_solo"
        self.epsilon = max(self.min_epsilon, self.epsilon * self.decay_rate)
        return action
