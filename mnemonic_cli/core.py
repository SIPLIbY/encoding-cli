from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import base64
import os

class SecretEncryption:
    @staticmethod
    def encrypt(message: str, password: str) -> str:
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = kdf.derive(password.encode())
        aesgcm = AESGCM(key)
        nonce = os.urandom(12)
        encrypted = aesgcm.encrypt(nonce, message.encode(), None)
        result = salt + nonce + encrypted
        return base64.b64encode(result).decode('utf-8')
    
    @staticmethod
    def decrypt(encrypted_data: str, password: str) -> str:
        data = base64.b64decode(encrypted_data.encode())
        salt = data[:16]
        nonce = data[16:28]
        encrypted = data[28:]
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = kdf.derive(password.encode())
        aesgcm = AESGCM(key)
        decrypted = aesgcm.decrypt(nonce, encrypted, None)
        return decrypted.decode('utf-8') 