def is_palindrome(string):
    if isinstance(string, int):
        string = str(string)
    return string[:] == string[::-1]

print(is_palindrome("test"))
print(is_palindrome("abba"))