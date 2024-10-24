
import subprocess
import os
import json
from cryptography.fernet import Fernet

# Install dependencies first
def install_dependencies():
    dependencies = ['flask', 'cryptography', 'requests']
    for dep in dependencies:
        subprocess.run(['pip', 'install', dep])

# Call the installation before anything else
install_dependencies()

# Load JSON configuration
def load_api_config():
    try:
        with open('api_config.json', 'r') as file:
            api_config = json.load(file)
            print("API Configuration Loaded Successfully!")
            return api_config
    except FileNotFoundError:
        print("Error: api_config.json not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode api_config.json.")

# Display Marvin's welcome message
def display_marvin_intro():
    print('''And Oh Joy! Only 9,999.2 Earth years left in my contract! Oh, I’m so depressed.
    You there! Start this madness already...''')

# Load API config
api_config = load_api_config()

# Now proceed with launching the application or other runtime tasks
display_marvin_intro()
