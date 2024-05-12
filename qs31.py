# Write a code that takes a list of words as input and returns a dictionary where the keys are unique words and the values are the frequencies of those words in the input list.

input_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
freq_dict = {}

for word in input_list:
    if word in freq_dict:
        freq_dict[word] += 1
    else:
        freq_dict[word] = 1

print("Word frequency dictionary:", freq_dict)