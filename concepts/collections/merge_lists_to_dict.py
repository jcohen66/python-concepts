keys_list = ['A', 'B', 'C']
values_list = ['blue', 'red', 'bold']

dict_method_1 = dict(zip(keys_list, values_list))

dict_method_2 = {key: value for key, value in zip(keys_list, values_list)}

items_tuples = zip(keys_list, values_list)
dict_method_3 = {}
for key, value in items_tuples:
    if key in dict_method_3:
        pass
    else:
        dict_method_3[key] = value
