
import openai
import psycopg2

class TaskFlowAutomation:
    def assign_task(self, task_description, agent_list):
        prompt = f"Assign the following task: {task_description}, to the most suitable agents from the following list: {agent_list}."
        response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=200)
        assignment = response.choices[0].text.strip()
        return assignment

    def monitor_and_start_tasks(self, agent_list):
        prompt = f"Monitor the following agents and start new tasks as soon as resources become available: {agent_list}."
        response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=200)
        monitoring_plan = response.choices[0].text.strip()
        return monitoring_plan
