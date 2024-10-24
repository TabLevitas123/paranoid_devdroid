
from cryptography.fernet import Fernet

class EncryptionManager:
    def __init__(self, key=None):
        # Generate a new key if not provided
        self.key = key if key else Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_data(self, data):
        if isinstance(data, str):
            data = data.encode()  # Convert string to bytes
        return self.cipher.encrypt(data)

    def decrypt_data(self, encrypted_data):
        try:
            return self.cipher.decrypt(encrypted_data).decode()  # Convert back to string
        except Exception as e:
            print("Decryption failed:", e)
            return None

# Example Usage
if __name__ == "__main__":
    encryptor = EncryptionManager()
    secret_message = "This is a highly confidential message."
    encrypted = encryptor.encrypt_data(secret_message)
    print("Encrypted:", encrypted)
    decrypted = encryptor.decrypt_data(encrypted)
    print("Decrypted:", decrypted)
