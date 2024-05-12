# Implement a code to find and remove duplicates from a list while preserving the original order of elements.

my_list = [1, 2, 2, 3, 3, 7,5,5, 6]

seen = set()
unique_list = []

for item in my_list:
    if item not in seen:
        seen.add(item)
        unique_list.append(item)

print("List after removing duplicates: ", unique_list)