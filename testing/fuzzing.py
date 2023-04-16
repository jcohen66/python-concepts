# Brute force values until code breaks!

import random
import string

def generate_random_string(length:int) -> str:
    characters:str = string.ascii_letters + string.digits + string.punctuation
    result_string: str = ''.join(random.choice(characters) for _ in range(length))
    
    return result_string

def fuzzer() -> str:
    while True:
        yield generate_random_string(random.randint(1,100))
        
def sample_function(input_str: str) -> int:
    try:
        if '!!!' in input_str:
            raise Exception('Bad input')
        return 0
    except Exception as e:
        print('Error:', e)
        return 1
    
def main():
    i: int = 0
    for input_str in fuzzer():
        i += 1
        result: int = sample_function(input_str)
        if result == 1:
            print(f'Run ${i}: Cause -> {input_str}')
            break
    
if __name__ == '__main__':
    # print(generate_random_string(10))
    main()