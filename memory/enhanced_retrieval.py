
import psycopg2

def retrieve_weighted_memories(task_id, weight_factor=1.0):
    """
    Retrieve memories weighted by relevance scores, adjusted by a given weight factor.
    """
    try:
        connection = psycopg2.connect(
            host='database-1-instance-1.c34ewagcc44a.us-east-2.rds.amazonaws.com',
            database='prof_e_esher',
            user='postgres',
            password='Lopside6902'
        )
        cursor = connection.cursor()
        
        # Fetch and weight memories by their relevance score
        cursor.execute(
            "SELECT * FROM memory_logs WHERE task_id = %s ORDER BY relevance DESC", (task_id,)
        )
        memories = cursor.fetchall()
        # Apply weight factor to relevance scores
        weighted_memories = [(mem[0], mem[1], mem[2], mem[3] * weight_factor) for mem in memories]
        
        cursor.close()
        connection.close()
        return weighted_memories
    except Exception as e:
        return f"Failed to retrieve weighted memories: {e}"


def retrieve_context_based_memories(task_id, context_info):
    """
    Retrieve memories based on task context (e.g., recent activities, agent actions).
    """
    try:
        connection = psycopg2.connect(
            host='database-1-instance-1.c34ewagcc44a.us-east-2.rds.amazonaws.com',
            database='prof_e_esher',
            user='postgres',
            password='Lopside6902'
        )
        cursor = connection.cursor()
        
        # Fetch memories with context information as a filter (example: recent tasks)
        cursor.execute(
            "SELECT * FROM memory_logs WHERE task_id = %s AND context = %s ORDER BY relevance DESC",
            (task_id, context_info)
        )
        memories = cursor.fetchall()
        
        cursor.close()
        connection.close()
        return memories
    except Exception as e:
        return f"Failed to retrieve context-based memories: {e}"
