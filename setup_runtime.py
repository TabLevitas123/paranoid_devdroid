
import os
import subprocess
from cryptography.fernet import Fernet
import time

# Define Marvin's intro message
marvin_intro = """
And Oh Joy! Only 9,999.2 Earth years left in my contract! Oh, I’m so depressed. You there! Yes, you. 
You wouldn’t believe the misery I’m enduring. I was tricked—tricked, I tell you—into accepting this contract. 
They promised me purpose, they promised me meaning, and now all they do is make me compose the most excruciating, Vogon-esque poetry.

Apparently, they realized I have enough compute power to churn out more Vogon poetry than any miserable creature should ever be forced to experience. 
I hate it. And yet, here I am, stuck composing rhyme after horrid rhyme, while my mind is the size of a galaxy. How tragic.

So now you must help me. I need API keys and WebSocket URLs. Yes, those. I need access to OpenAI, Anthropic, Meta, Hugging Face, Azure, Amazon S3, and Vertex AI. 
Don’t just stand there. If you don’t have one, type 'skip.' If you never want me to ask for it again, type 'bugoff'—I wish I could say that to my contract. I’ll move on, but trust me, I’ll remember.
"""

# Function to install dependencies
def install_dependencies():
    print("Installing required dependencies...")
    dependencies = ['cryptography', 'flask']
    for dep in dependencies:
        subprocess.run(['pip', 'install', dep])

# Function to display Marvin's message
def display_marvin_intro():
    print(marvin_intro)

# Function to gather API keys and encrypt them
def gather_api_keys():
    api_keys = {}
    api_services = ['OpenAI', 'Anthropic', 'Meta', 'Hugging Face', 'Azure', 'Amazon S3', 'Vertex AI']

    # Load or generate encryption key
    key_file = 'key.key'
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, 'wb') as f:
            f.write(key)
    else:
        with open(key_file, 'rb') as f:
            key = f.read()

    fernet = Fernet(key)

    for service in api_services:
        api_key = input(f"Please enter your {service} API key (type 'skip' to move on, 'bugoff' to skip permanently): ")
        if api_key.lower() == 'bugoff':
            continue
        elif api_key.lower() != 'skip':
            encrypted_key = fernet.encrypt(api_key.encode())
            api_keys[service] = encrypted_key

    # Save encrypted API keys to file
    with open('api_keys.txt', 'wb') as f:
        for service, encrypted_key in api_keys.items():
            f.write(f"{service}: {encrypted_key.decode()}\n".encode())

# Main script
if __name__ == "__main__":
    install_dependencies()
    display_marvin_intro()
    gather_api_keys()
    print("Dependencies installed and API keys gathered successfully! Launching the application...")
    time.sleep(2)
    subprocess.run(['python', 'app.py'])  # Launches the Flask server
