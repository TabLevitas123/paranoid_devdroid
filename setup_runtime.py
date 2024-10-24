
import subprocess
import os
import json
from cryptography.fernet import Fernet
import re  # For regex-based credential validation

# Install dependencies including React
def install_dependencies():
    dependencies = [
        'flask', 'cryptography', 'requests', 'psycopg2',
        'react', 'react-dom', 'axios'  # Adding React dependencies
    ]
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

# Function to validate API credentials based on specific syntax
def validate_api_credentials(api_name, credentials):
    api_patterns = {
        'aws': r'^[A-Z0-9]{20}$',  # Example pattern for AWS Access Keys
        'github': r'^github_pat_[A-Za-z0-9_]+$',  # Pattern for GitHub personal access tokens
        'postgres': r'^[a-zA-Z0-9!@#$%^&*()_+=-]{8,}$'  # Example: Simple password validation
    }

    if api_name in api_patterns:
        pattern = api_patterns[api_name]
        if re.match(pattern, credentials):
            print(f"Credentials for {api_name} are syntactically correct.")
            return True
        else:
            print(f"Error: Invalid credentials syntax for {api_name}.")
            return False
    else:
        print(f"No validation rules available for {api_name}.")
        return False

# Example usage of validation function
db_config = load_db_config()
if db_config:
    validate_api_credentials('postgres', db_config.get('password', ''))

# Display Marvin's welcome message
def display_marvin_intro():
    print("And Oh Joy! Only 9,999.2 Earth years left in my contract! Oh, I'm so depressed. You there, yes you, run along and give me something to do!")

display_marvin_intro()
