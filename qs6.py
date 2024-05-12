# Write a code to perform basic string compression using the counts of repeated characters

def compress_string(input_string):
    compressed_string = ""
    count = 1
    for i in range(len(input_string)):
        if i + 1 < len(input_string) and input_string[i] == input_string[i + 1]:
            count += 1
        else:
            compressed_string += input_string[i] + str(count)
            count = 1  
    if len(compressed_string) >= len(input_string):
        return input_string
    else:
        return compressed_string


input_string = input("Enter a string : ")
compressed_result = compress_string(input_string)
print("Compressed string:", compressed_result)
