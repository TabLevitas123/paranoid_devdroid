
import time
import psycopg2

class RealTimeMonitoring:
    def __init__(self):
        self.connection = psycopg2.connect(
            host='database-1-instance-1.c34ewagcc44a.us-east-2.rds.amazonaws.com',
            database='prof_e_esher',
            user='postgres',
            password='Lopside6902'
        )
        self.cursor = self.connection.cursor()

    def monitor_agent_performance(self, agent_id):
        """
        Monitor an agent's task performance in real time, including decision-making and memory usage.
        """
        while True:
            self.cursor.execute("SELECT * FROM agent_performance WHERE agent_id = %s ORDER BY timestamp DESC LIMIT 1", (agent_id,))
            performance = self.cursor.fetchone()
            print(f"Real-time performance for Agent {agent_id}: {performance}")
            
            # Sleep for a while before the next check (simulate real-time monitoring)
            time.sleep(10)

    def monitor_memory_usage(self):
        """
        Monitor memory usage, tracking the number of relevant memories accessed or logged by agents.
        """
        while True:
            self.cursor.execute("SELECT COUNT(*) FROM memory_logs")
            memory_count = self.cursor.fetchone()
            print(f"Real-time memory usage: Total logged memories: {memory_count[0]}")
            
            # Sleep for a while before the next check
            time.sleep(10)

    def monitor_decision_making(self, agent_id):
        """
        Monitor agent decision-making, tracking choices made during tasks.
        """
        while True:
            self.cursor.execute("SELECT * FROM decisions WHERE agent_id = %s ORDER BY timestamp DESC LIMIT 1", (agent_id,))
            decision = self.cursor.fetchone()
            print(f"Real-time decision for Agent {agent_id}: {decision}")
            
            # Sleep for a while before the next check
            time.sleep(10)

    def close_connection(self):
        """
        Close the database connection.
        """
        self.cursor.close()
        self.connection.close()
