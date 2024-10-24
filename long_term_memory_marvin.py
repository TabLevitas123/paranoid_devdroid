
import sqlite3

class LongTermMemoryMarvin:
    def __init__(self):
        self.conn = sqlite3.connect('marvin_memory.db')
        self.cursor = self.conn.cursor()
        self.memory_threshold = 1000  # Max number of entries
        self.cleanup_threshold = 800  # Number of entries to keep during cleanup

    def store_memory(self, memory_data):
        # Store new memory entry in the database
        self.cursor.execute("INSERT INTO memories (data) VALUES (?)", (memory_data,))
        self.conn.commit()
        self.check_memory_threshold()

    def check_memory_threshold(self):
        # Check if memory exceeds the cleanup threshold
        self.cursor.execute("SELECT COUNT(*) FROM memories")
        memory_count = self.cursor.fetchone()[0]
        if memory_count > self.memory_threshold:
            self.cleanup_memory()

    def cleanup_memory(self):
        # Cleanup old memory entries, keeping only the most recent
        self.cursor.execute(f"DELETE FROM memories WHERE id IN (SELECT id FROM memories ORDER BY id ASC LIMIT {self.memory_threshold - self.cleanup_threshold})")
        self.conn.commit()

    def retrieve_memory(self):
        # Retrieve all memories
        self.cursor.execute("SELECT * FROM memories ORDER BY id DESC")
        return self.cursor.fetchall()

# Example Usage
if __name__ == "__main__":
    marvin_memory = LongTermMemoryMarvin()
    for i in range(1100):  # Simulating 1100 memory entries
        marvin_memory.store_memory(f"Memory Entry {i}")
    print(marvin_memory.retrieve_memory())
