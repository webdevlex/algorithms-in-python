# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?


# Solution 1: With additional data structures
def is_unique_chars1(s):
    if len(s) > 128:
        return False

    char_set = [False] * 128
    for char in s:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True

    return True


# Solution 2: With additional data structures
def is_unique_chars2(s):
    checker = 0
    for char in s:
        val = ord(char) - ord("a")
        if checker & (1 << val) > 0:
            return False
        checker |= 1 << val
    return True


# Soution 3: If we are allowed to modify the input string, we could sort the string in
# O(n log(n)) time and then linearly check the string for neighboring characters
# that are identical. Be careful, though many sorting algorithms take up extra
# space.


input = "Test"

output1 = is_unique_chars1(input)
print(f'\nInput: "{input}"\noutput: {output1}')

output2 = is_unique_chars2(input)
print(f'\nInput: "{input}"\noutput: {output2}')
