
import openai

class HierarchicalTaskHandling:
    def prioritize_tasks(self, task_list):
        task_info = "\n".join([f"Task {task['id']}: Urgency - {task['urgency']}, Complexity - {task['complexity']}" for task in task_list])
        prompt = f"Prioritize the following tasks based on urgency and complexity:\n{task_info}"
        response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=200)
        prioritized_tasks = response.choices[0].text.strip()
        return prioritized_tasks
