# Develop a code that prompts the user to input two sets of strings. Then, print the symmetric difference of these two sets.

input_string1 = input("Enter strings separated by spaces for first set: ")
string_list1 = [s.strip() for s in input_string1.split()]
set1 = set(string_list1)

input_string2 = input("Enter strings separated by spaces for second set: ")
string_list2 = [s.strip() for s in input_string2.split()]
set2 = set(string_list2)

symmetric_differ = set1.symmetric_difference(set2)
print("Symmetric difference of the two sets:", symmetric_differ)