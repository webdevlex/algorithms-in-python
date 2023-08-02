# Check Permutation: Given two strings, write a method to decide if one is a
# permutation of the other.


# Solution 1
def sort_string(s):
    content = list(s)
    content.sort()
    return "".join(content)


def is_permutation1(s, t):
    if len(s) != len(t):
        return False
    return sort_string(s) == sort_string(t)


# Solution 2
def is_permutation2(str1, str2):
    if len(str1) != len(str2):
        return False

    chars = [0] * 128
    for char in str1:
        i = ord(char) - ord("a")
        chars[i] += 1

    for char in str2:
        i = ord(char) - ord("a")
        chars[i] -= 1
        if chars[i] < 0:
            return False

    return True


input1 = "Test"
input2 = "teTs"
print(f'\nInput: "{input1}", "{input2}"')

output = is_permutation1(input1, input2)
print(f"Output: {output}")

output = is_permutation2(input1, input2)
print(f"Output: {output}")
