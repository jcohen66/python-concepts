import timeit

def contains_a(input_var: str) -> bool:
    return 'a' in input_var.lower()

def comp_test():
    people: List[str] = ['Maria', 'Luigi', 'Toad', 'Bowser', 'Peach', 'Daisy', 'Shy Guy']
    new_people = [person for person in people if contains_a(person)]
    return new_people

def filter_test():
    people: List[str] = ['Maria', 'Luigi', 'Toad', 'Bowser', 'Peach', 'Daisy', 'Shy Guy']
    new_people = filter(contains_a, people)
    return list(new_people)


def main():
    people = ['Elon', 'Mark', 'Mario', 'Luigi']
    
    # Returns List
    new_list = [person for person in people if contains_a(person)]
    
    # Returns Iterable
    new_list2 = filter(contains_a, people)
    
    print(list(new_list2))
    
def get_time(func, name: str):
    speed = min(timeit.repeat(func, repeat=10, number=100_000))
    print(f'{name:10}: {round(speed, 4)} sec')
    
    return speed
    
def timed():
    filter_speed = get_time(func=filter_test, name='filter')
    comp_speed = get_time(func=comp_test, name='list comp')
    
    # Check the speed comparison
    percent_faster = round(100 * (1 - (filter_speed / comp_speed)), 2)
    print(percent_faster, '% faster')
    
    # Check that output is the same
    print('\nComp == Filter:', comp_test() == filter_test())
        
if __name__ == '__main__':
    #main()
    timed()
    