
import psycopg2
import openai

class TaskMemoryExpansion:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        openai.api_key = openai_api_key

    def retrieve_task_specific_memory(self, task_id, step_description):
        """
        Retrieve memories specific to a task step from the database, with LLM-enhanced relevance.
        """
        try:
            connection = psycopg2.connect(
                host='database-1-instance-1.c34ewagcc44a.us-east-2.rds.amazonaws.com',
                database='prof_e_esher',
                user='postgres',
                password='Lopside6902'
            )
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM memory_logs WHERE task_id = %s", (task_id,))
            memories = cursor.fetchall()
            cursor.close()
            connection.close()

            # Use LLM to analyze and retrieve task-specific memories
            prompt = f"Given the task step: {step_description}, retrieve relevant memories from the following data:\n{memories}"
            response = openai.Completion.create(
                engine="gpt-4",
                prompt=prompt,
                max_tokens=300
            )
            refined_memories = response.choices[0].text.strip()
            return refined_memories
        
        except Exception as e:
            return f"Failed to retrieve task-specific memories: {e}"

    def share_memory_between_agents(self, sender_agent_id, receiver_agent_id, task_memory):
        """
        Simulate sharing memory between agents during a task, mediated by LLMs.
        """
        prompt = f"Agent {sender_agent_id} wants to share the following memory with Agent {receiver_agent_id}: {task_memory}. Facilitate the sharing process."
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=200
        )
        memory_sharing_response = response.choices[0].text.strip()
        return memory_sharing_response

