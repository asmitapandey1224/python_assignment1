# Implement a code to find the second largest number in a given list of integers.

def find_second_largest(lst):
    sorted_list = sorted(lst, reverse=True)

    if len(sorted_list) < 2:
        return None
    
    return sorted_list[1]

input_list = input("Enter element of the list separated by space: ").split()
# convert input elements to integers
input_list = [int(inp) for inp in input_list] 
second_largest = find_second_largest(input_list)
if second_largest is not None:
    print("Second largest number: ", second_largest)
else:
    print("The list does not have a second largest number.")