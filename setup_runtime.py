
import subprocess
from cryptography.fernet import Fernet
import os
from api_key_management_plugin import encrypt_keys, store_encrypted_key

# Display Marvin's welcome message
def display_marvin_intro():
    print('''And Oh Joy! Only 9,999.2 Earth years left in my contract! Oh, I’m so depressed.
    You there! Yes, you. You wouldn’t believe the misery I’m enduring... (entire message)''')

# Install dependencies
def install_dependencies():
    dependencies = ['flask', 'cryptography', 'requests']
    for dep in dependencies:
        subprocess.run(['pip', 'install', dep])

# Function to handle API keys
def request_api_keys():
    services = ['OpenAI', 'Anthropic', 'Meta', 'Hugging Face', 'Azure', 'Amazon S3', 'Vertex AI']
    bugoff_list = []
    api_keys = {}
    for service in services:
        if service not in bugoff_list:
            key = input(f"Enter the {service} API key (or type 'skip' to pass, 'bugoff' to never ask again): ")
            if key.lower() == 'skip':
                continue
            elif key.lower() == 'bugoff':
                bugoff_list.append(service)
            else:
                encrypted_key = encrypt_keys(key)
                store_encrypted_key(service, encrypted_key)
                api_keys[service] = encrypted_key
    return api_keys

if __name__ == "__main__":
    install_dependencies()
    display_marvin_intro()
    request_api_keys()

    # Launch Flask app after keys are managed
    subprocess.run(['python', 'app.py'])
