
import psycopg2

def memory_garbage_collection():
    """
    Clean up irrelevant or outdated memories from the database.
    Memories older than a defined time threshold will be deleted.
    """
    try:
        connection = psycopg2.connect(
            host='database-1-instance-1.c34ewagcc44a.us-east-2.rds.amazonaws.com',
            database='prof_e_esher',
            user='postgres',
            password='Lopside6902'
        )
        cursor = connection.cursor()
        
        # Define a time threshold (e.g., memories older than 30 days)
        cursor.execute("DELETE FROM memory_logs WHERE timestamp < NOW() - INTERVAL '30 days'")
        deleted_count = cursor.rowcount
        connection.commit()
        cursor.close()
        connection.close()
        return f"Garbage collection complete: {deleted_count} outdated memories removed."
    except Exception as e:
        return f"Failed to perform garbage collection: {e}"
