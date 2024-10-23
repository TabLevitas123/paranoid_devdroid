
import openai

class MultiAgentTaskPrioritization:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        openai.api_key = openai_api_key

    def prioritize_tasks(self, agent_data, task_list):
        """
        Use LLM to prioritize tasks based on task urgency, complexity, and agent availability.
        """
        task_descriptions = "\n".join([f"Task {task['id']}: {task['description']}, Urgency: {task['urgency']}, Complexity: {task['complexity']}" for task in task_list])
        agent_info = "\n".join([f"Agent {agent['id']}: Availability - {agent['availability']}" for agent in agent_data])
        prompt = f"Given the following tasks:\n{task_descriptions}\nand the following agents:\n{agent_info}, prioritize the tasks for optimal execution."
        
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=250
        )
        prioritized_tasks = response.choices[0].text.strip()
        return prioritized_tasks

    def dynamic_task_shifting(self, agent_id, current_task, new_task):
        """
        Allow agents to dynamically shift tasks if a higher-priority task arises during execution.
        """
        prompt = f"Agent {agent_id} is currently working on Task {current_task}, but Task {new_task} has higher urgency. Should Agent {agent_id} switch tasks?"
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=100
        )
        task_shift_decision = response.choices[0].text.strip()
        return task_shift_decision

