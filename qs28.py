# Create a code that defines two sets of integers. Then, print the union, intersection, and difference of these two sets.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Union = ", set1 | set2)
print("Intersection = ", set1 & set2)
print("Difference (set1 - set2) = ", set1 - set2)
print("Difference (set2 - set1) = ", set2 - set1)