
import openai

class LLMIntelligentAgent:
    def __init__(self, agent_id, llm_api_key):
        self.agent_id = agent_id
        self.llm_api_key = llm_api_key
        openai.api_key = llm_api_key

    def ask_llm(self, prompt):
        """
        Communicate with the LLM to get task insights or generate decisions.
        """
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",  # Can be updated based on the LLM in use
                prompt=prompt,
                max_tokens=150
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"LLM failed to respond: {e}"

    def execute_task_with_llm(self, task_description):
        """
        Use LLM to generate a plan for task execution.
        """
        prompt = f"Plan and execute the following task: {task_description}"
        response = self.ask_llm(prompt)
        print(f"LLM Task Plan: {response}")
        # Perform task based on LLM's plan (simulation)
        return response

    def make_decision_with_llm(self, memory_context):
        """
        Use LLM to make decisions based on task memory context.
        """
        prompt = f"Given the following context, what should be the next step?
Context: {memory_context}"
        response = self.ask_llm(prompt)
        print(f"LLM Decision: {response}")
        return response
