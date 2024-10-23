
import time
import psycopg2

def monitor_agent_performance(agent_id):
    try:
        connection = psycopg2.connect(
            host='database-1-instance-1.c34ewagcc44a.us-east-2.rds.amazonaws.com',
            database='prof_e_esher',
            user='postgres',
            password='Lopside6902'
        )
        cursor = connection.cursor()
        
        while True:
            # Query to monitor agent's task performance
            cursor.execute("SELECT * FROM agent_performance WHERE agent_id = %s ORDER BY timestamp DESC LIMIT 1", (agent_id,))
            performance = cursor.fetchone()
            print(f"Real-time monitoring for Agent {agent_id}: {performance}")
            
            # Sleep for a while before the next check (simulate real-time monitoring)
            time.sleep(10)
            
    except Exception as e:
        print(f"Failed to monitor agent: {e}")
    finally:
        cursor.close()
        connection.close()

def monitor_memory_usage():
    try:
        connection = psycopg2.connect(
            host='database-1-instance-1.c34ewagcc44a.us-east-2.rds.amazonaws.com',
            database='prof_e_esher',
            user='postgres',
            password='Lopside6902'
        )
        cursor = connection.cursor()
        
        while True:
            # Query to monitor memory usage from logs
            cursor.execute("SELECT COUNT(*) FROM memory_logs")
            memory_count = cursor.fetchone()
            print(f"Real-time memory usage: Total logged memories: {memory_count[0]}")
            
            # Sleep for a while before the next check
            time.sleep(10)
            
    except Exception as e:
        print(f"Failed to monitor memory usage: {e}")
    finally:
        cursor.close()
        connection.close()
