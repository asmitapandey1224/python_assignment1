# Write a code that inverts a dictionary, swapping keys and values. Ensure that the inverted dictionary correctly handles cases where multiple keys have the same value by storing the keys as a list in the inverted dictionary.

def invert_dictionary(dictionary):
    inverted_dict = {}
    for key, value in dictionary.items():
        if value in inverted_dict:
            inverted_dict[value].append(key)
        else:
            inverted_dict[value] = [key]
    return inverted_dict


input_dict = {'apple': 3, 'banana': 2, 'orange': 1, 'grape': 3}
inverted_dict = invert_dictionary(input_dict)
print("Inverted dictionary:", inverted_dict)
