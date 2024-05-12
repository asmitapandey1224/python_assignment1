# Write a code that takes a dictionary as input and returns a sorted version of it based on the values. You can choose whether to sort in ascending or descending order.

def sort_dictionary_by_values(dictionary, reverse=False):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=reverse))
    return sorted_dict


input_dict = {'apple': 3, 'banana': 2, 'orange': 1, 'pineapple': 5, 'grape': 4}
sorted_dict_asc = sort_dictionary_by_values(input_dict)  
print("Sorted dictionary (ascending order):", sorted_dict_asc)

sorted_dict_desc = sort_dictionary_by_values(input_dict, reverse=True)  
print("Sorted dictionary (descending order):", sorted_dict_desc)
