# write a code to count the number of words in a string

def count_words(input_string):
    words = input_string.split()
    return len(words)


input_string = input("Enter a string : ")
num_words = count_words(input_string)
print("Number of words in the string:", num_words)
