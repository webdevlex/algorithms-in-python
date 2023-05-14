def palindromePermutation(str):
    chars = [0] * 26
    numOdds = 0
    for char in str:
        i = getIndex(char)
        if i != -1:
            chars[i] += 1
            if chars[i] % 2 == 1:
                numOdds += 1
            else:
                numOdds -= 1

    print(numOdds)
    return numOdds < 2


def getIndex(char):
    a = ord("a")
    z = ord("z")
    val = ord(char)

    if val >= a and val <= z:
        return val - a
    return -1


input = "aaba"
output = palindromePermutation(input)
print(f'\nInput: "{input}"')
print(f"Output: {output}")
