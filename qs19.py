# Create a code to find the union of two lists without duplicates.

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

union_result = list1 + list2

my_set = set(union_result)
my_list = list(my_set)

print(my_list)