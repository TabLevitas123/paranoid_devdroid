
import openai

class LLMFeedbackLoop:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        openai.api_key = openai_api_key

    def analyze_task_outcome(self, task_description, task_outcome):
        """
        Use LLM to analyze the task outcome and provide feedback for improvement.
        """
        prompt = f"Given the task: {task_description} and the outcome: {task_outcome}, provide feedback on how the agent could improve in the future."
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=200
        )
        feedback = response.choices[0].text.strip()
        return feedback

    def refine_agent_strategy(self, agent_strategy, feedback):
        """
        Use LLM to refine the agent's strategy based on feedback.
        """
        prompt = f"Given the current agent strategy: {agent_strategy}, and the feedback: {feedback}, suggest improvements to the strategy."
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=150
        )
        refined_strategy = response.choices[0].text.strip()
        return refined_strategy

    def create_feedback_loop(self, task_description, task_outcome, agent_strategy):
        """
        Complete feedback loop for the agent to learn from task outcomes and refine its strategy.
        """
        feedback = self.analyze_task_outcome(task_description, task_outcome)
        refined_strategy = self.refine_agent_strategy(agent_strategy, feedback)
        return {
            "feedback": feedback,
            "refined_strategy": refined_strategy
        }
