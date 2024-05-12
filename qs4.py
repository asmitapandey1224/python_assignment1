# write a code to check if two given strings are anagrams of each other.

def check_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    char_count = {}
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False 

    for count in char_count.values():
        if count != 0:
            return False

    return True


string1 = input("Enter string 1 : ")
string2 = input("Enter string 2 : ")
if check_anagrams(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")