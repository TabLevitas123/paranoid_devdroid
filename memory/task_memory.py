
import psycopg2

def retrieve_task_specific_memories(task_id, cluster_priority=True):
    """
    Retrieve memories for a task with the option to prioritize clusters.
    """
    try:
        connection = psycopg2.connect(
            host='database-1-instance-1.c34ewagcc44a.us-east-2.rds.amazonaws.com',
            database='prof_e_esher',
            user='postgres',
            password='Lopside6902'
        )
        cursor = connection.cursor()
        
        if cluster_priority:
            # Fetch memories based on clusters, prioritize cluster relevance
            cursor.execute(
                "SELECT * FROM memory_logs WHERE task_id = %s ORDER BY relevance DESC", (task_id,)
            )
        else:
            # Fetch memories without considering clusters
            cursor.execute(
                "SELECT * FROM memory_logs WHERE task_id = %s", (task_id,)
            )
        
        memories = cursor.fetchall()
        cursor.close()
        connection.close()
        return memories
    except Exception as e:
        return f"Failed to retrieve task-specific memories: {e}"
