import hashlib

print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)

h = hashlib.sha256("hello".encode("ascii"))
print(h)

h = hashlib.new("SHA256")
h.update(b"Hello World")
print(h.digest)
print(h.hexdigest())  # recommended


correct_password = "MyPassword123567"
h = hashlib.new("SHA256")

h.update(correct_password.encode())
password_hash = h.hexdigest()
print(password_hash)

user_input = "MyPassword123567"
h = hashlib.new("SHA256")
h.update(user_input.encode())
print(h.hexdigest())
