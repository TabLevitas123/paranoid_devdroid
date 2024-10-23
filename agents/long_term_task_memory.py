
import openai

class LongTermTaskMemory:
    def retrieve_long_term_memories(self, task_description):
        prompt = f"Retrieve long-term memories related to the following task: {task_description}, to improve the decision-making for this multi-step task."
        response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=200)
        long_term_memories = response.choices[0].text.strip()
        return long_term_memories
