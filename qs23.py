# Write a code to concatenate two tuples. The function should take two tuples as input and return a new tuple containing elements from both input tuples.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

concatenated_list = list(tuple1) + list(tuple2)

concatenated_tuple = tuple(concatenated_list)

print("Concatenated tuple:", concatenated_tuple)