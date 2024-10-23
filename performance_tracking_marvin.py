
class PerformanceTrackingMarvin(AdvancedLoggingMarvin):
    def __init__(self, name, task_complexity, accuracy_level=3, learning_rate=0.1, discount_factor=0.95):
        super().__init__(name, task_complexity, accuracy_level, learning_rate, discount_factor)
        self.task_start_time = None

    def start_task(self):
        self.task_start_time = time.time()
        self.log_event(event_type="Task Start", details=f"Task started with complexity {self.task_complexity} at accuracy level {self.accuracy_level}.")

    def complete_task(self):
        task_duration = time.time() - self.task_start_time
        self.log_event(event_type="Task Complete", details=f"Task completed in {task_duration:.2f} seconds.")
        return task_duration

    def store_logs_to_db(self):
        connection = psycopg2.connect(host=hostname, database=database, user=username, password=password)
        cursor = connection.cursor()
        for log in self.logs:
            insert_log_query = 'INSERT INTO task_logs (timestamp, event_type, details) VALUES (%s, %s, %s);'
            cursor.execute(insert_log_query, (log['timestamp'], log['event_type'], log['details']))
        connection.commit()
        cursor.close()
        connection.close()
        print("Logs stored in the database.")
