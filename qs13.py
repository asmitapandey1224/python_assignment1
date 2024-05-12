# Create a code to count the occurrences of each element in a list and return a dictionary with elements as keys and their counts as values.

my_list = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]
count = {}

for item in my_list:
    count[item] = count.get(item, 0) +1

print("Occurrences of each element: ", count)