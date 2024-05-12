# Create a code that takes a tuple and two integers as input. The function should return a new tuple containing elements from the original tuple within the specified range of indices.

input_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
start_index = 2
end_index = 5

if start_index < 0 or end_index >= len(input_tuple) or start_index > end_index:
    print(None)

new_tuple = input_tuple[start_index:end_index+1]

if new_tuple is not None:
    print("New tuple containing elements within the specified range:", new_tuple)
else:
    print("Invalid range of indices specified.")