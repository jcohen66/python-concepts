"""
See https://stuvel.eu/python-rsa-doc/usage.html
"""

import rsa


with open("my_key_pair.pem", mode="rb") as privatefile:
    keydata = privatefile.read()

# Bob generates key pair and gives the public
# key to Alice.
privkey = rsa.PrivateKey.load_pkcs1(keydata)
pubkey = rsa.PublicKey.load_pkcs1(keydata)

# Alice writes a message and encodes since RSA
# cant act on strings.
plaintext_message = "This is my secret message."
encoded_message = plaintext_message.encode("utf8")

# Get the signature of the message
signature = rsa.sign(encoded_message, privkey, "SHA-1")

# Alice encrypts the message using the public key she
# got from Bob.
encrypted_message = rsa.encrypt(encoded_message, pubkey)

# Bob receives the encrypted message and decrypts
# it using his private key.
decrypted_message = rsa.decrypt(encrypted_message, privkey)
decoded_message = decrypted_message.decode("utf8")

# Bob verifies the message against the signature
verified = (decrypted_message, signature, pubkey)

print(privkey)
print(pubkey)
print(plaintext_message)
print(encoded_message)
print(encrypted_message)
print(signature)
print(decrypted_message)
print(decoded_message)
print(verified)
