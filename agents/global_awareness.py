
import openai

class GlobalAwareness:
    def reflect_on_system_performance(self):
        prompt = "Reflect on the overall performance of the system and suggest improvements to enhance efficiency, collaboration, and resource usage."
        response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=300)
        self_reflection_plan = response.choices[0].text.strip()
        return self_reflection_plan
