d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# method 1
new_dict = dict(sorted(d.items(), key=lambda item: item[1]))

