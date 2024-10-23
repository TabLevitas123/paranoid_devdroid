
import numpy as np

class MetaLearningAgent:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.task_memory = {}
    
    def update_memory(self, task_id, outcome):
        """
        Meta-learning logic: Agents update their memory based on task outcomes.
        """
        if task_id not in self.task_memory:
            self.task_memory[task_id] = []
        self.task_memory[task_id].append(outcome)

    def prioritize_task(self, task_id):
        """
        Prioritize tasks based on learning outcomes (e.g., successful task completions).
        """
        if task_id in self.task_memory:
            successes = sum([1 for outcome in self.task_memory[task_id] if outcome == 'success'])
            return successes / len(self.task_memory[task_id])
        return 0

class QLearningAgent:
    def __init__(self, agent_id, alpha=0.1, gamma=0.9):
        self.agent_id = agent_id
        self.q_table = {}
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor

    def choose_action(self, state):
        """
        Choose action based on the Q-table for the current state.
        """
        if state not in self.q_table:
            self.q_table[state] = np.zeros(2)  # Initialize Q-values for actions
        return np.argmax(self.q_table[state])

    def update_q_table(self, state, action, reward, next_state):
        """
        Q-learning update rule to optimize agent actions.
        """
        if state not in self.q_table:
            self.q_table[state] = np.zeros(2)
        if next_state not in self.q_table:
            self.q_table[next_state] = np.zeros(2)
        # Q-Learning formula: Q(s, a) = Q(s, a) + alpha * [reward + gamma * max(Q(s', a')) - Q(s, a)]
        self.q_table[state][action] += self.alpha * (reward + self.gamma * np.max(self.q_table[next_state]) - self.q_table[state][action])

