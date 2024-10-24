
import subprocess
import os
from cryptography.fernet import Fernet

# Install dependencies first
def install_dependencies():
    dependencies = ['flask', 'cryptography', 'requests']
    for dep in dependencies:
        subprocess.run(['pip', 'install', dep])

# Call the installation before anything else
install_dependencies()

# Display Marvin's welcome message
def display_marvin_intro():
    print('''And Oh Joy! Only 9,999.2 Earth years left in my contract! Oh, I’m so depressed.
    You there! Yes, you. You wouldn’t believe the misery I’m enduring... But alas, let’s proceed.''')

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
                # Placeholder for encryption or any key management
                encrypted_key = Fernet.generate_key()  # Example encryption
                api_keys[service] = encrypted_key
    return api_keys

# Main function
if __name__ == "__main__":
    display_marvin_intro()

    # Manage API keys
    api_keys = request_api_keys()

    # Launch the Flask app
    print("Launching Flask app...")
    subprocess.run(['python', 'app.py'])
