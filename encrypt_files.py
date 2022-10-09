from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
from passlib.hash import argon2



def encfile(file_name, password, iterations=10000):
    password = bytes(password, 'utf-8')
    salt = bytes(0)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA3_512(),
        length=32,
        salt=salt,
        iterations=iterations,
        backend=default_backend())

    key = base64.urlsafe_b64encode(kdf.derive(password))

    f = Fernet(key)

    with open(file_name, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)

    with open(file_name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decfile(file_name, password, iterations=10000):
    password1 = bytes(password, 'utf-8')
    salt = bytes(0)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA3_512(),
        length=32,
        salt=salt,
        iterations=iterations,
        backend=default_backend())

    key = base64.urlsafe_b64encode(kdf.derive(password1))
    f = Fernet(key)

    with open(file_name,'rb') as original_file:
        original = original_file.read()

    decrypted = f.decrypt(original)

    with open (file_name,'wb') as decrypted_file:
        decrypted_file.write(decrypted)

def hash_for_password():
    # generate new salt, hash password
    hash = argon2.hash("2")
    print(hash)

    # ver = argon2.verify("password1", hash)

# hash_for_password()
# from cryptography.fernet import Fernet
# key = Fernet.generate_key()
# cipher_suite = Fernet(key)
# cipher_text = cipher_suite.encrypt(b"this is really secret message. Not for prying eyes.")
# print(cipher_text)
# plain_text = cipher_suite.decrypt(cipher_text)
# print(plain_text)

