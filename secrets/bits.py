import secrets

random = secrets.randbits(16)
print(random)

# 32 bytes of randomness
token = secrets.token_bytes(32)
print(token)

token = secrets.token_hex(32)
print(token)

token = secrets.token_urlsafe(32)
print(token)
print(f'www.website.com/authenticate/{token}')

