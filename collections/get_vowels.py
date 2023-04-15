def get_vowels(string):
    return [item for item in string if item in 'aeiou']

if __name__ == "__main__":
    print(get_vowels("assert"))
    print(get_vowels("football"))
