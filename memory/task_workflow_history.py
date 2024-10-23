
import psycopg2
import openai

class TaskWorkflowHistory:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        openai.api_key = openai_api_key

    def log_task_execution(self, agent_id, task_id, task_description, task_outcome):
        """
        Log a task execution, including task description, outcome, and agent involved.
        """
        try:
            connection = psycopg2.connect(
                host='database-1-instance-1.c34ewagcc44a.us-east-2.rds.amazonaws.com',
                database='prof_e_esher',
                user='postgres',
                password='Lopside6902'
            )
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO task_history (agent_id, task_id, task_description, task_outcome, timestamp) VALUES (%s, %s, %s, %s, NOW())",
                (agent_id, task_id, task_description, task_outcome)
            )
            connection.commit()
            cursor.close()
            connection.close()
            return f"Task {task_id} for Agent {agent_id} has been successfully logged."
        
        except Exception as e:
            return f"Failed to log task execution: {e}"

    def retrieve_task_history(self, task_description):
        """
        Retrieve relevant task history based on similar task descriptions using LLM to compare.
        """
        try:
            connection = psycopg2.connect(
                host='database-1-instance-1.c34ewagcc44a.us-east-2.rds.amazonaws.com',
                database='prof_e_esher',
                user='postgres',
                password='Lopside6902'
            )
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM task_history")
            task_histories = cursor.fetchall()
            cursor.close()
            connection.close()

            # Use LLM to find relevant past tasks
            task_history_text = "\n".join([f"Task {history[1]}: {history[2]}, Outcome: {history[3]}" for history in task_histories])
            prompt = f"Given the task: {task_description}, retrieve relevant past tasks from the following history:\n{task_history_text}"
            response = openai.Completion.create(
                engine="gpt-4",
                prompt=prompt,
                max_tokens=300
            )
            relevant_histories = response.choices[0].text.strip()
            return relevant_histories
        
        except Exception as e:
            return f"Failed to retrieve task history: {e}"
