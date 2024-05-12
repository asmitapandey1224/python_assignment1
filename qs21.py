# Write a code that takes two tuples as input and returns a new tuple containing elements that are common to both input tuples.

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

set1 = set(tuple1)
set2 = set(tuple2)

common_element = set1 & set2
common_tuple = tuple(common_element)

print(common_tuple)