# write a code to find all occurrences of a given substring within another string

def find_occurrences(main_string, sub_string):
    occurrences = []
    start_index = 0

    while True:
        index = main_string.find(sub_string, start_index)
        if index == -1:  
            break
        occurrences.append(index)
        start_index = index + 1  

    return occurrences


main_string = input("Enter the main string : ")
sub_string = input("Enter the sub-string : ")
result = find_occurrences(main_string, sub_string)
print("Occurrences of '{}' in '{}':".format(sub_string, main_string))
print(result)
