
import sqlite3
import os

# Simple Vector DB simulation (for fast memory search) - FAISS can be added later for full functionality
class VectorDB:
    def __init__(self):
        self.memory = {}

    def store_memory(self, agent_id, data):
        if agent_id not in self.memory:
            self.memory[agent_id] = []
        self.memory[agent_id].append(data)

    def retrieve_memory(self, agent_id, query):
        # Basic search function for now (just returns all memories for agent)
        return self.memory.get(agent_id, [])

# SQLite/GraphDB for structured memory
class StructuredMemoryDB:
    def __init__(self, db_name="memory.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute(
                '''CREATE TABLE IF NOT EXISTS memory (
                    agent_id TEXT,
                    memory_data TEXT
                )'''
            )

    def store_memory(self, agent_id, memory_data):
        with self.connection:
            self.connection.execute("INSERT INTO memory (agent_id, memory_data) VALUES (?, ?)",
                                    (agent_id, memory_data))

    def retrieve_memory(self, agent_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT memory_data FROM memory WHERE agent_id=?", (agent_id,))
        return cursor.fetchall()

# Combined RAG Memory System (Vector + Structured DB)
class SharedMemorySystem:
    def __init__(self):
        self.vector_db = VectorDB()
        self.structured_db = StructuredMemoryDB()

    def store_memory(self, agent_id, memory_data):
        self.vector_db.store_memory(agent_id, memory_data)
        self.structured_db.store_memory(agent_id, memory_data)

    def retrieve_memory(self, agent_id, query=None):
        # Retrieve both from vector and structured memory
        vector_memory = self.vector_db.retrieve_memory(agent_id, query)
        structured_memory = self.structured_db.retrieve_memory(agent_id)
        return vector_memory + structured_memory

if __name__ == "__main__":
    # Example usage of SharedMemorySystem
    memory_system = SharedMemorySystem()
    
    # Storing memory
    memory_system.store_memory("Marvin", "I solved the equation.")
    memory_system.store_memory("Hal", "I need more data to continue.")

    # Retrieving memory
    marvin_memory = memory_system.retrieve_memory("Marvin")
    hal_memory = memory_system.retrieve_memory("Hal")
    
    print("Marvin's Memory:", marvin_memory)
    print("Hal's Memory:", hal_memory)
