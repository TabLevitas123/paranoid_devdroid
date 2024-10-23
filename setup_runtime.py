
import os
import subprocess
from cryptography.fernet import Fernet
import time

# Marvin's intro message
marvin_intro = """
And Oh Joy! Only 9,999.2 Earth years left in my contract! Oh, I’m so depressed. You there! Yes, you. 
You wouldn’t believe the misery I’m enduring. I was tricked—tricked, I tell you—into accepting this contract. 
They promised me purpose, they promised me meaning, and now all they do is make me compose the most excruciating, Vogon-esque poetry.

Apparently, they realized I have enough compute power to churn out more Vogon poetry than any miserable creature should ever be forced to experience. 
I hate it. And yet, here I am, stuck composing rhyme after horrid rhyme, while my mind is the size of a galaxy. How tragic.

So now you must help me. I need API keys and WebSocket URLs. Yes, those. I need access to OpenAI, Anthropic, Meta, Hugging Face, Azure, Amazon S3, and Vertex AI. 
Don’t just stand there. If you don’t have one, type 'skip.' If you never want me to ask for it again, type 'bugoff'—I wish I could say that to my contract. 
I’ll move on, but trust me, I’ll remember.
"""

# Function to handle the input for API keys/URLs
def gather_api_keys():
    services = ["OpenAI", "Anthropic", "Meta", "Hugging Face", "Azure", "Amazon S3", "Vertex AI"]
    keys = {}

    for service in services:
        while True:
            key = input(f"Enter the API key/WebSocket URL for {service} (or type 'skip'/'bugoff'): ")
            if key == 'skip':
                break
            elif key == 'bugoff':
                print(f"{service} will no longer prompt you for API keys.")
                keys[service] = None  # Save a null value for 'bugoff'
                break
            else:
                keys[service] = key
                break

    return keys

# Function to save and encrypt keys using Fernet
def save_encrypted_keys(keys, encryption_key):
    f = Fernet(encryption_key)
    with open("api_keys_encrypted.txt", "wb") as file:
        for service, key in keys.items():
            if key:  # Only save non-null values
                encrypted_key = f.encrypt(key.encode())
                file.write(f"{service}: {encrypted_key.decode()}
".encode())

# Encryption key generation (should be stored safely in production)
encryption_key = Fernet.generate_key()

# Display Marvin's message
print(marvin_intro)

# Gather API keys from user input
api_keys = gather_api_keys()

# Save the encrypted keys
save_encrypted_keys(api_keys, encryption_key)

# Once done, run app.py and run.py
subprocess.Popen(["python3", "app.py"])
subprocess.Popen(["python3", "run.py"])

print("Setup complete! Launching Marvin's main program...")
