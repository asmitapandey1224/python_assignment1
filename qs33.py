# Write a code to access a value in a nested dictionary. The function should take the dictionary and a list of keys as input, and return the corresponding value. If any of the keys do not exist in the dictionary, the function should return None.

def access_nested_value(dictionary, keys):
    nested_dict = dictionary
    for key in keys:
        if key in nested_dict:
            nested_dict = nested_dict[key]
        else:
            return None
    return nested_dict


nested_dictionary = {'outer': {'inner1': {'value1': 1,'value2': 2},'inner2': {'value3': 3,'value4': 4}}}


keys_to_access = ['outer', 'inner1', 'value2']
result = access_nested_value(nested_dictionary, keys_to_access)
print("Accessed value:", result)