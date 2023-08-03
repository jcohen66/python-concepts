# import pandas as pd
names = ['Mariya', 'Gendalf', 'Batman']
profs = ['programmer', 'Wizard', 'Superhero']

my_dict = {}

for (key, value) in zip(names, profs):
    my_dict[key] = value

print(my_dict)

my_dict = {
    names[i]: profs[i] for i in range(len(names))
}

# names_pd = pd.DataFrame(['Mariya', 'Gendalf', 'Batman'])
# profs_pd = pd.DataFrame(['programmer', 'Wizard', 'Superhero'])

# my_dict = {key: value for (key, value) in zip(names[0], profs[0])}

# my_dict = {
#     names[0][i]: profs[0][i] for i in range(len(names))
# }

my_dict = {
    "Spider": "photographer",
    "Bat": "philanthropist",
    "Wonder Wom": "nurse"
}

my_dict = {(key + 'man' if key == 'Spiderman' else 'Superman'):
           (val if val != 'photographer' else 'journalist')
           for (key, val) in my_dict.items()}
print(my_dict)
