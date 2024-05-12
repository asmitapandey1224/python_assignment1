# Develop a code that prompts the user to input two sets of strings. Then, print the elements that are present in the first set but not in the second set.

set1 = input("Enter strings separated by commas for the first set: ")
string_list1 = [x.strip() for x in set1.split(",")]
string_set1 = set(string_list1)

set2 = input("Enter strings separated by commas for the second set: ")
string_list2 = [x.strip() for x in set2.split(",")]
string_set2 = set(string_list2)

differ = string_set1 - string_set2
print("Elements present in the first set but not in the second set:", differ)