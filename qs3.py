# Write a code to check if  a given string is a palindrome or not

def is_palindrome(input_string):
    input_string = input_string.replace(" ", "").lower()
    return input_string == input_string[::-1]

string = input("Enter a string : ")
result = is_palindrome(string)
if result:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


