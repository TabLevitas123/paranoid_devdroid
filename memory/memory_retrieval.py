
import psycopg2

def retrieve_task_memories(task_id):
    try:
        connection = psycopg2.connect(
            host='database-1-instance-1.c34ewagcc44a.us-east-2.rds.amazonaws.com',
            database='prof_e_esher',
            user='postgres',
            password='Lopside6902'
        )
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM memory_logs WHERE task_id = %s ORDER BY relevance DESC", (task_id,)
        )
        memories = cursor.fetchall()
        cursor.close()
        connection.close()
        return memories
    except Exception as e:
        return f"Failed to retrieve memories: {e}"
