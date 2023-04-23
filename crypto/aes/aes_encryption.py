from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

simple_key = get_random_bytes(32)
print(simple_key)

salt = b'\xeaB\x89\xa1q\x8d\x82\x90q\x17\x01Y\xfd\xc76\xf0iv\x92\xce\xdd\xc6\x13\xbcm\x01\xe5\x956r\x96`'
password = 'mypassword'

key = PBKDF2(password, salt, dkLen=32)

message = b'Hello Secret World!'

cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))
print(ciphered_data)

with open('encrypted.bin', 'wb') as f:
    f.write(cipher.iv)
    f.write(ciphered_data)
    
with open('encrypted.bin', 'rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()
    
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print(original)

with open('key.bin', 'wb') as f:
    f.write(key)