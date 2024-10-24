
import os
import hashlib
from cryptography.fernet import Fernet

class SecurityManager:
    def __init__(self):
        self.encryption_key = Fernet.generate_key()
        self.cipher = Fernet(self.encryption_key)

    def hash_password(self, password):
        # Hash the password using SHA-256
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password, hashed_password):
        return self.hash_password(password) == hashed_password

    def encrypt_data(self, data):
        return self.cipher.encrypt(data.encode())

    def decrypt_data(self, encrypted_data):
        try:
            return self.cipher.decrypt(encrypted_data).decode()
        except Exception as e:
            print(f"Decryption failed: {e}")
            return None

# Example Usage
if __name__ == "__main__":
    security = SecurityManager()
    password = "SecurePassword123"
    hashed_pw = security.hash_password(password)
    print(f"Hashed Password: {hashed_pw}")
    print(f"Password verification: {security.verify_password('SecurePassword123', hashed_pw)}")

    # Encryption and decryption
    secret_data = "Sensitive data to be encrypted"
    encrypted_data = security.encrypt_data(secret_data)
    print(f"Encrypted Data: {encrypted_data}")
    decrypted_data = security.decrypt_data(encrypted_data)
    print(f"Decrypted Data: {decrypted_data}")
