
import psycopg2

def log_memory(task_id, description, status):
    try:
        connection = psycopg2.connect(
            host='database-1-instance-1.c34ewagcc44a.us-east-2.rds.amazonaws.com',
            database='prof_e_esher',
            user='postgres',
            password='Lopside6902'
        )
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO memory_logs (task_id, description, status) VALUES (%s, %s, %s)",
            (task_id, description, status)
        )
        connection.commit()
        cursor.close()
        connection.close()
        return f"Memory logged for task {task_id} with status {status}."
    except Exception as e:
        return f"Failed to log memory: {e}"
