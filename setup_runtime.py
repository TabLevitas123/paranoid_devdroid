
import subprocess
import os
import json
from cryptography.fernet import Fernet

# Install dependencies first
def install_dependencies():
    dependencies = ['flask', 'cryptography', 'requests', 'psycopg2']  # Added psycopg2 for PostgreSQL access
    for dep in dependencies:
        subprocess.run(['pip', 'install', dep])

# Call the installation before anything else
install_dependencies()

# Load JSON configuration for database credentials
def load_db_config():
    try:
        with open('db_config.json', 'r') as file:
            db_config = json.load(file)
            print("Database Configuration Loaded Successfully!")
            return db_config
    except FileNotFoundError:
        print("Error: db_config.json not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode db_config.json.")

# Display Marvin's welcome message
def display_marvin_intro():
    print('''And Oh Joy! Only 9,999.2 Earth years left in my contract! Oh, I’m so depressed.
    You there! Start this madness already...''')

# Load database config (hostname, db_name, username, password)
db_config = load_db_config()

# Example: Print the loaded database configuration (remove this in production)
if db_config:
    print(f"DB Host: {db_config['hostname']}")
    print(f"DB Name: {db_config['db_name']}")
    print(f"DB User: {db_config['username']}")

# Now proceed with launching the application or other runtime tasks
display_marvin_intro()
