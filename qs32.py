# Write a code that takes two dictionaries as input and merges them into a single dictionary. If there are common keys, the values should be added together.

dict1 = {'apple': 3, 'banana': 2, 'orange': 1}
dict2 = {'banana': 1, 'pineapple': 2, 'grape': 1}

merged_dict = {}

for key, value in dict1.items():
    merged_dict[key] = value

for key, value in dict2.items():
    if key in merged_dict:
        merged_dict[key] += value
    else:
        merged_dict[key] = value

print("Merged dictionary:", merged_dict)