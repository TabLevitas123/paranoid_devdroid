
from cryptography.fernet import Fernet
import os

class APIKeyManager:
    def __init__(self, key_file='key.key', api_key_file='api_keys.txt'):
        self.key_file = key_file
        self.api_key_file = api_key_file
        self.fernet = None
        self.load_or_generate_key()

    def load_or_generate_key(self):
        # Load the encryption key from a file or generate a new one
        if not os.path.exists(self.key_file):
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as f:
                f.write(key)
        else:
            with open(self.key_file, 'rb') as f:
                key = f.read()
        self.Fernet = Fernet(key)
    def encrypt_and_store_keys(self, api_keys):
        # Encrypt and store API keys in a text file
        with open(self.api_key_file, 'wb') as f:
            for service, key in api_keys.items():
                encrypted_key = self.Fernet.encrypt(key.encode())
                f.write(f"{service}: {encrypted_key.decode()}\n".encode())

    def retrieve_keys(self):
        # Retrieve and decrypt the stored API keys
        if not os.path.exists(self.api_key_file):
            print("No API keys found.")
            return {}

        decrypted_keys = {}
        with open(self.api_key_file, 'rb') as f:
            lines = f.readlines()
            for line in lines:
                service, encrypted_key = line.decode().strip().split(': ')
                decrypted_key = self.Fernet.decrypt(encrypted_key.encode()).decode()
                decrypted_keys[service] = decrypted_key
        return decrypted_keys

# Example usage:
if __name__ == "__main__":
    api_key_manager = APIKeyManager()
    
    # Example to encrypt and store keys
    api_keys = {
        'OpenAI': 'YOUR_OPENAI_KEY',
        'Anthropic': 'YOUR_ANTHROPIC_KEY'
    }
    api_key_manager.encrypt_and_store_keys(api_keys)
    
    # Retrieve the decrypted keys
    stored_keys = api_key_manager.retrieve_keys()
    print("Decrypted API keys:", stored_keys)
