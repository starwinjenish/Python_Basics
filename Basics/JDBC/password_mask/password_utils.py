from encrypt_once import generate_key
from cryptography.fernet import Fernet


class fakeStar(str):
    def __str__(self):
        return "*******"
    def __repr__(self):
        return "*******"



def load_key():
    return open ('secret.key','rb').read()

def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode())

def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypted =  f.decrypt(encrypted_password).decode()
    return fakeStar(decrypted)

def get_decrypt_password():
    encrypt_password = " "
    return decrypt_password(encrypt_password)



    