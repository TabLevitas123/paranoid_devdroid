
import psycopg2
import openai

class ProactiveMemoryManagement:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        openai.api_key = openai_api_key

    def predict_upcoming_memories(self, task_description):
        prompt = f"Given the following task description, predict which memories from the memory logs will be needed: {task_description}."
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=150
        )
        memory_prediction = response.choices[0].text.strip()
        return memory_prediction

    def retrieve_predicted_memories(self, predicted_memories):
        try:
            connection = psycopg2.connect(
                host='database-1-instance-1.c34ewagcc44a.us-east-2.rds.amazonaws.com',
                database='prof_e_esher',
                user='postgres',
                password='Lopside6902'
            )
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM memory_logs WHERE description IN ({predicted_memories})")
            retrieved_memories = cursor.fetchall()
            cursor.close()
            connection.close()
            return retrieved_memories if retrieved_memories else "No relevant memories found."
        
        except Exception as e:
            return f"Failed to retrieve predicted memories: {e}"
