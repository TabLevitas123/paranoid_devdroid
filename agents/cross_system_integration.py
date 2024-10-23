
import openai

class CrossSystemIntegration:
    def integrate_with_external_systems(self, system_description, external_systems):
        system_info = "\n".join([f"System: {system}" for system in external_systems])
        prompt = f"Integrate the following system: {system_description}, with these external systems:\n{system_info}."
        response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=300)
        integration_plan = response.choices[0].text.strip()
        return integration_plan
