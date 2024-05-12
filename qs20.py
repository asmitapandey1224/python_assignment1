# Write a code to shuffle a given list randomly without using any built-in shuffle functions.
import random

my_list = [1, 2, 3, 4, 5]

shuffled_list = my_list[:]

n = len(shuffled_list)

for i in range(n-1, 0, -1):
    j = random.randint(0, i)
    shuffled_list[i], shuffled_list[j] = shuffled_list[j], shuffled_list[i]

print("Original List: ", my_list)
print("Shuffled List: ",shuffled_list)