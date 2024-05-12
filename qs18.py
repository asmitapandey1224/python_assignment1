# Implement a code to find the intersection of two given list.

l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]

set1 = set(l1)
set2 = set(l2)

intersection_set = set1.intersection(set2)

intersection_list = list(intersection_set)

print(intersection_list)