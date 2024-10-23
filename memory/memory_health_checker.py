
import openai
import psycopg2

class MemoryHealthChecker:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        openai.api_key = openai_api_key

    def check_memory_health(self):
        """
        Analyze memory clusters and determine their relevance for future tasks using LLM.
        """
        try:
            connection = psycopg2.connect(
                host='database-1-instance-1.c34ewagcc44a.us-east-2.rds.amazonaws.com',
                database='prof_e_esher',
                user='postgres',
                password='Lopside6902'
            )
            cursor = connection.cursor()
            cursor.execute("SELECT id, description FROM memory_logs")
            memories = cursor.fetchall()
            cursor.close()
            connection.close()

            # Use LLM to analyze memory health and relevance
            prompt = f"Analyze the health and relevance of the following memories for future tasks:\n{memories}"
            response = openai.Completion.create(
                engine="gpt-4",
                prompt=prompt,
                max_tokens=300
            )
            memory_health_report = response.choices[0].text.strip()
            return memory_health_report
        
        except Exception as e:
            return f"Failed to check memory health: {e}"

    def recommend_memory_cleanup(self, memory_health_report):
        """
        Recommend cleanup of irrelevant memories based on health check results.
        """
        prompt = f"Based on the following memory health report: {memory_health_report}, recommend which memories should be removed."
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=150
        )
        cleanup_recommendations = response.choices[0].text.strip()
        return cleanup_recommendations
