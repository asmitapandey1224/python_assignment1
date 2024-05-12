# Write a code to reverse a list in-place without using any built-in reverse functions.

lis = [1, 2, 3, 4, 5]
print("Original List: ", lis)

n = len(lis)

for i in range(n // 2):
    lis[i], lis[n - i - 1] = lis[n - i - 1], lis[i]

print("Reversed list: ", lis)