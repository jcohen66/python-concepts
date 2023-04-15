def byte_size(string):
    return len(string.encode('utf-8'))

if __name__ == "__main":
    print(byte_size("hello"))
    print(byte_size("Python Programming"))