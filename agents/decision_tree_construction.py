
import openai

class DecisionTreeConstruction:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        openai.api_key = openai_api_key

    def construct_decision_tree(self, task_description, potential_decisions):
        """
        Use LLM to construct a decision tree for a complex multi-step task.
        """
        decisions = "\n".join([f"Decision {i+1}: {decision}" for i, decision in enumerate(potential_decisions)])
        prompt = f"Construct a decision tree for the following task: {task_description}, with the potential decisions:\n{decisions}. Provide the possible consequences of each decision."
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=300
        )
        decision_tree = response.choices[0].text.strip()
        return decision_tree

    def evaluate_decision_path(self, task_description, decision_path):
        """
        Evaluate the consequences of a specific decision path chosen by the agent.
        """
        prompt = f"Evaluate the consequences of the following decision path for the task: {task_description}: {decision_path}. Provide potential outcomes."
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=150
        )
        decision_outcomes = response.choices[0].text.strip()
        return decision_outcomes
