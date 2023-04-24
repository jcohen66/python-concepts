import hashlib

CORRECT_HASH = "1356246234634573674356223452345234523452435"

with open("Everything-1.3.1.1022.x85-Setup.exe", "rb") as f:
    file_bytes = f.read()
    h = hashlib.sha256()
    h.update(file_bytes)
    file_hash = h.hexdigest()


print(file_hash == CORRECT_HASH)

# 3.11
digest = hashlib.file_digest(f, "sha256")
