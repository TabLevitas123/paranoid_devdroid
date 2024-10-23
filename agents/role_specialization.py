
import openai

class RoleSpecialization:
    def assign_roles(self, task_description, agent_list):
        agent_info = "\n".join([f"Agent {agent['id']}: Strength - {agent['strength']}" for agent in agent_list])
        prompt = f"Assign roles to the following agents based on their strengths and the requirements of the task: {task_description}.\n{agent_info}"
        response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=200)
        role_assignment = response.choices[0].text.strip()
        return role_assignment
