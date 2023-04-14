import secrets

user_input = 'abc123'
password = 'abc123'

# Takes into account timing to avoid timing attacks.
if secrets.compare_digest(user_input, password):
    print('You are now logged in!')
    
    
# Uses highest quality resources from OS
sr = secrets.SystemRandom()
print(sr)

