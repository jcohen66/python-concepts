import rsa

with open('public.pem', 'rb') as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())
    
with open('private.pem', 'rb') as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())
    
    
encrypted_message = open("encrypted.message", "rb").read()

clear_message = rsa.decrypt(encrypted_message, private_key)
print(clear_message)
