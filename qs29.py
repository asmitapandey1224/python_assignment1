# Write a code that takes a tuple and an element as input. The function should return the count of occurrences of the given element in the tuple.

input_tuple = (1, 2, 2, 3, 2, 4, 5, 2)

element = 2
occurrences = input_tuple.count(element)
print("Occurrences of", element, "in the tuple:", occurrences)