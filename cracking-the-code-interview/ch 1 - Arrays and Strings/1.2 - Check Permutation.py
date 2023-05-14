def checkPermutation(str1, str2):
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
output = checkPermutation(input1, input2)
print(f'\nInput: "{input1}", "{input2}"')
print(f"Output: {output}")
