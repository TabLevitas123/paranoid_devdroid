
import openai

class LLMTaskBreakdown:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        openai.api_key = openai_api_key

    def break_down_task(self, complex_task_description):
        """
        Use LLM to break down a complex task into smaller, manageable steps.
        """
        prompt = f"Break down the following complex task into smaller, manageable steps:\n{complex_task_description}"
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=250
        )
        task_steps = response.choices[0].text.strip()
        return task_steps

    def assist_agent_in_task(self, agent_id, complex_task_description):
        """
        Assist the agent by breaking down the complex task and assigning subtasks.
        """
        task_steps = self.break_down_task(complex_task_description)
        print(f"Task Breakdown for Agent {agent_id}:\n{task_steps}")
        return task_steps
