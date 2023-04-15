def is_palindrome(string):
    # check if string is same as reverse.
    return string == string[::-1]

print(is_palindrome("abba"))
print(is_palindrome("car"))