# write a code to concatenate two strings without using the + operator

def concatenate_strings(str1, str2):
    return "{} {}".format(str1, str2)


string1 = input("Enter a string : ")
string2 = input("Enter an another string : ")
result = concatenate_strings(string1, string2)
print("Concatenated string:", result)