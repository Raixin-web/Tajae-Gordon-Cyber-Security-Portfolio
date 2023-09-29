import base64
import hashlib
from Crypto.Cipher import AES

class AES256:
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()
        self.iv = b'\x0e\xb9e?\xd54b\x9c\xe5\x00p\xf9\xd8\xec.\xa4'

    def encrypt(self, plaintext):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)

        padding_length = 16 - (len(plaintext) % 16)
        plaintext += chr(padding_length) * padding_length

        ciphertext = cipher.encrypt(plaintext.encode())
        return base64.b64encode(self.iv + ciphertext)
    
    def decrypt(self, ciphertext):
        ciphertext = base64.b64decode(ciphertext)

        iv = ciphertext[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        plaintext = cipher.decrypt(ciphertext[16:]).decode()
        padding_length = ord(plaintext[-1])
        return plaintext[:-padding_length]



