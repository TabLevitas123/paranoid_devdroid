
import openai
import psycopg2

class LLMEnhancedMemorySystem:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        openai.api_key = openai_api_key

    def refine_memory_clusters(self, cluster_data, task_description):
        """
        Use LLM to reason over memory clusters and adjust them based on task relevance.
        """
        prompt = f"Given the task: {task_description}, refine the following memory clusters for better relevance:\n{cluster_data}"
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=300
        )
        refined_clusters = response.choices[0].text.strip()
        return refined_clusters

    def retrieve_llm_enhanced_memories(self, task_id, task_description):
        """
        Retrieve memories with LLM-enhanced reasoning, improving relevance based on the task.
        """
        try:
            connection = psycopg2.connect(
                host='database-1-instance-1.c34ewagcc44a.us-east-2.rds.amazonaws.com',
                database='prof_e_esher',
                user='postgres',
                password='Lopside6902'
            )
            cursor = connection.cursor()
            
            # Fetch memory logs related to the task
            cursor.execute("SELECT * FROM memory_logs WHERE task_id = %s ORDER BY relevance DESC", (task_id,))
            memories = cursor.fetchall()
            cursor.close()
            connection.close()
            
            # Use LLM to reason over the retrieved memories for better relevance
            prompt = f"Given the task: {task_description}, refine the following memories for better relevance:\n{memories}"
            response = openai.Completion.create(
                engine="gpt-4",
                prompt=prompt,
                max_tokens=300
            )
            refined_memories = response.choices[0].text.strip()
            return refined_memories
        except Exception as e:
            return f"Failed to retrieve LLM-enhanced memories: {e}"
