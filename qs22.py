# Create a code that prompts the user to enter two sets of integers separated by commas. Then, print the intersection of these two sets.

set1 = input("Enter integers for the first set separated by commas: ")
integer_list1 = [int(x.strip()) for x in set1.split(",")]
integer_set1 = set(integer_list1)

set2 = input("Enter integers for the second set separated by commas: ")
integer_list2 = [int(x.strip()) for x in set2.split(",")]
integer_set2 = set(integer_list2)

intersection = integer_set1.intersection(integer_set2)
print("Intersection of the two sets: ", intersection)