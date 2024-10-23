
import openai

class AdaptiveTaskComplexity:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        openai.api_key = openai_api_key

    def analyze_task_complexity(self, task_description):
        """
        Use LLM to analyze the complexity of a task and suggest adaptations.
        """
        prompt = f"Analyze the complexity of the following task and suggest how to adapt to its complexity: {task_description}."
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=150
        )
        complexity_analysis = response.choices[0].text.strip()
        return complexity_analysis

    def adjust_task_execution(self, task_id, task_description, complexity_analysis):
        """
        Based on the complexity analysis, adjust task execution by recommending more resources or dividing the task.
        """
        prompt = f"Given the complexity analysis: {complexity_analysis}, recommend adjustments to task {task_id} for better execution."
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=200
        )
        adjustment_recommendation = response.choices[0].text.strip()
        return adjustment_recommendation

    def run_complexity_analysis_and_adjustment(self, task_id, task_description):
        """
        Full cycle of analyzing task complexity and adjusting execution.
        """
        complexity_analysis = self.analyze_task_complexity(task_description)
        adjustment = self.adjust_task_execution(task_id, task_description, complexity_analysis)
        return {
            "complexity_analysis": complexity_analysis,
            "adjustment": adjustment
        }
