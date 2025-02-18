my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

sorted_keys = sorted(my_dict, key=my_dict.get, reverse=True)

print(sorted_keys[0],sorted_keys[1],sorted_keys[2])