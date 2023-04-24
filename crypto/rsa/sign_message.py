import rsa

with open('public.pem', 'rb') as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())
    
with open('private.pem', 'rb') as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())
    
message = "I have a new account on Twitter which is @madeupname9987615"

signature = rsa.sign(message.encode(), private_key, "SHA-256")
with open("signature", "wb") as f:
    f.write(signature)