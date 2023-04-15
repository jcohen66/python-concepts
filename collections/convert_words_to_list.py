import re

def to_list(string, pattern = '[a-zA-Z]+'):
    # Filters out special characters.
    return re.findall(pattern, string)

if __name__ == '__main__':
    print(to_list("Python"))
    print(to_list("Are you a programmer?"))
    
