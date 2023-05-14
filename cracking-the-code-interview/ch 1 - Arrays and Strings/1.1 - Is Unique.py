def isUnique(str):
    if len(str) > 128:
        return False

    chars = [False] * 128
    for char in str:
        i = ord(char) - ord("a")
        if chars[i]:
            return False
        chars[i] = True

    return True


input = "Test"
output = isUnique(input)
print(f'\nInput: "{input}"\nOutput: {output}')
