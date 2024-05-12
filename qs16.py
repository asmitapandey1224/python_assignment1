# Create a code to check if a given list is sorted (either in ascending or descending order) or not.


my_list = [3, 1, 4, 2, 5]

if all(my_list[i] <= my_list[i + 1] for i in range(len(my_list) - 1)):
        print("Ascending")
    
if all(my_list[i] >= my_list[i + 1] for i in range(len(my_list) - 1)):
    print("Descending")
    
print("Not sorted")