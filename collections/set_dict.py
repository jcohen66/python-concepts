my_str = "Timothy Unkert"

my_set = {char for char in my_str}

print(len(my_str))
print(len(my_set))

my_state_list = [
    "Colorado",
    "Connecticut",
    "California",
    "Colorado",
    "Vermont",
    "New York",
    "Colorado",
    "Vermont"
]

my_state_set = {state for state in my_state_list}

print(my_state_list)
print(my_state_set)


my_ages_dict = {
    "Sarah": 50,
    "Tim": 47,
    "Joe": 11,
    "Will": 18,
    "Ben": 46
}

current_year = 2023

my_birth_year_dict = {k:current_year - v for k,v in my_ages_dict.items()}

print(my_birth_year_dict)