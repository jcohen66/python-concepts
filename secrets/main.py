import secrets
import string

# cryptographically secure.
random = secrets.randbelow(100)
print(random)

random_choice = secrets.choice([1,2,3,4,5])
print(random_choice)

def generate_password(length: int):
    chars: str = string.ascii_letters + string.digits + string.punctuation
    password: str = ''.join(secrets.choice(chars) for _ in range(length))
    
    print('Generated password: ', password )
    
    
generate_password(14)