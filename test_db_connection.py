
import psycopg2
import json

# Load database configuration
def load_db_config():
    try:
        with open('db_config.json', 'r') as file:
            db_config = json.load(file)
            return db_config
    except FileNotFoundError:
        print("Error: db_config.json not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Failed to decode db_config.json.")
        return None

# Establish database connection
def connect_to_db():
    db_config = load_db_config()
    if not db_config:
        return None
    
    try:
        # Connect to the PostgreSQL database using credentials from db_config.json
        connection = psycopg2.connect(
            host=db_config['hostname'],
            database=db_config['db_name'],
            user=db_config['username'],
            password=db_config['password']
        )
        print("Database connection established successfully!")
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

# Test the database connection by executing a simple query
def test_db_connection():
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT version();")  # Example query to check DB version
            version = cursor.fetchone()
            print(f"PostgreSQL version: {version}")
            cursor.close()
        except Exception as e:
            print(f"Error executing query: {e}")
        finally:
            connection.close()

# Run the test
if __name__ == "__main__":
    test_db_connection()
