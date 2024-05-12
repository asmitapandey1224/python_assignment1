# Write a code to remove all occurrences of a specific element from a list.

element = input("Enter element of the list separated by space: ").split()
element = [int(elem) for elem in element] 

element_to_remove = int(input("Enter the element to remove : "))

remove_element = [item for item in element if item != element_to_remove]

if element_to_remove:
    print("List after removing all occurrences of {}: {}".format(element_to_remove, remove_element))
else:
    print("Element {} not found in the list.".format(element_to_remove))