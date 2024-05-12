# Write a code to determine if a string has all unique characters

def has_unique_characters(input_string):
    encountered = set()

    for char in input_string:
        if char in encountered:
            return False
        else:
            encountered.add(char)
    return True


string1 = input("Enter string 1 : ")

print("String '{}' has all unique characters: {}".format(string1, has_unique_characters(string1)))
