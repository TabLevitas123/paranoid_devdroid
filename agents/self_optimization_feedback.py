
import openai

class SelfOptimizationFeedback:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        openai.api_key = openai_api_key

    def request_feedback(self, agent_id, task_description, task_outcome):
        prompt = f"Agent {agent_id} has completed the task: {task_description} with the outcome: {task_outcome}. Provide feedback and suggest how Agent {agent_id} can improve."
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=150
        )
        feedback = response.choices[0].text.strip()
        return feedback

    def implement_feedback(self, agent_id, feedback):
        prompt = f"Based on the following feedback for Agent {agent_id}: {feedback}, suggest how the agent should adjust their strategy for future tasks."
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=150
        )
        strategy_adjustment = response.choices[0].text.strip()
        return strategy_adjustment

    def run_self_optimization_cycle(self, agent_id, task_description, task_outcome):
        feedback = self.request_feedback(agent_id, task_description, task_outcome)
        optimized_strategy = self.implement_feedback(agent_id, feedback)
        return {
            "feedback": feedback,
            "optimized_strategy": optimized_strategy
        }
