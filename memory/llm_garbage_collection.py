
import openai
import psycopg2

class LLMGarbageCollection:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        openai.api_key = openai_api_key

    def evaluate_memory_relevance(self, memory_description):
        """
        Use LLM to evaluate the relevance of a memory based on its description.
        """
        prompt = f"Evaluate the relevance of the following memory and suggest whether it should be retained or removed:\n{memory_description}"
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=100
        )
        evaluation = response.choices[0].text.strip()
        return evaluation

    def perform_garbage_collection(self):
        """
        Perform garbage collection by analyzing old memories and removing irrelevant ones based on LLM feedback.
        """
        try:
            connection = psycopg2.connect(
                host='database-1-instance-1.c34ewagcc44a.us-east-2.rds.amazonaws.com',
                database='prof_e_esher',
                user='postgres',
                password='Lopside6902'
            )
            cursor = connection.cursor()
            
            # Fetch old memories from the database (older than 30 days, as an example)
            cursor.execute("SELECT id, description FROM memory_logs WHERE timestamp < NOW() - INTERVAL '30 days'")
            old_memories = cursor.fetchall()

            # Analyze each memory with LLM
            for memory_id, description in old_memories:
                relevance_evaluation = self.evaluate_memory_relevance(description)
                if "remove" in relevance_evaluation.lower():
                    # If LLM suggests removal, delete the memory
                    cursor.execute("DELETE FROM memory_logs WHERE id = %s", (memory_id,))
                    print(f"Memory {memory_id} removed based on LLM evaluation.")
            
            connection.commit()
            cursor.close()
            connection.close()
            return "Garbage collection completed."
        
        except Exception as e:
            return f"Failed to perform garbage collection: {e}"
