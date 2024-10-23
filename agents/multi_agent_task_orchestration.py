
import openai

class MultiAgentTaskOrchestration:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        openai.api.key = openai_api_key

    def divide_task_among_agents(self, task_description, agent_list):
        agent_info = "\n".join([f"Agent {agent['id']}: Strength - {agent['strength']}" for agent in agent_list])
        prompt = f"Given the task: {task_description}, and the following agents:\n{agent_info}, divide the task into subtasks and assign them to the most suitable agents."
        response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=250)
        task_division = response.choices[0].text.strip()
        return task_division

    def synchronize_agents(self, agent_list):
        agent_progress = "\n".join([f"Agent {agent['id']}: Task Progress - {agent['progress']}%" for agent in agent_list])
        prompt = f"Synchronize the following agents based on their progress:\n{agent_progress}. Ensure that they complete their assigned subtasks in the correct order."
        response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=200)
        synchronization_plan = response.choices[0].text.strip()
        return synchronization_plan

    def execute_task_orchestration(self, task_description, agent_list):
        task_division = self.divide_task_among_agents(task_description, agent_list)
        synchronization = self.synchronize_agents(agent_list)
        return {
            "task_division": task_division,
            "synchronization_plan": synchronization
        }
