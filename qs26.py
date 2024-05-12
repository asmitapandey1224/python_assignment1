# Write a code that prompts the user to input two sets of characters. Then, print the union of these two sets.

input1 = input("Enter characters separated by spaces for the first set: ")
char_list1 = [c.strip() for c in input1.split()]
set1 = set(char_list1)

input2 = input("Enter characters separated by spaces for the first set: ")
char_list2 = [c.strip() for c in input2.split()]
set2 = set(char_list2)

union_set = set1 | set2
print("Union of the two sets:", union_set)