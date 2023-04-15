# Lock Your Files
#pip install cryptography

from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def Lock_file(file_name, key):
    with open(file_name, 'rb') as file:
        data = file.read()
    f = Fernet(key)
    encrypted_data = f.encrypt(data)
    with open(file_name, 'wb') as file:
        file.write(encrypted_data)
    print("File Lock...")
    
    
def Unlock_file(file_name, key):
    with open(file_name, 'rb') as file:
        data = file.read()
    f = Fernet(key)
    decrypted_data = f.decrypt(data)
    with open(file_name, 'wb') as file:
        file.write(decrypted_data)
    print("File Unlock...")
    
def print_file(file_name):
    with open(file_name, 'rb') as file:
        data = file.read()
    print(data)
    
key = generate_key()
Lock_file('test.txt', key)
print_file('test.txt')
Unlock_file('test.txt', key)