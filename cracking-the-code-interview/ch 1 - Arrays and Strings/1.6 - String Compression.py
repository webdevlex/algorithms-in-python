def stringCompression(givenStr):
    if compressedLength(givenStr) >= len(givenStr):
        return givenStr
    return compress(givenStr)


def compressedLength(givenStr):
    compressedLength = 0
    consecutiveCount = 0
    for i in range(len(givenStr)):
        consecutiveCount += 1
        if i + 1 >= len(givenStr) or givenStr[i] != givenStr[i + 1]:
            compressedLength += 1 + len(str(consecutiveCount))
            consecutiveCount = 0
    return compressedLength


def compress(givenStr):
    stringBuilder = []
    consecutiveCount = 0
    for i in range(len(givenStr)):
        consecutiveCount += 1
        if i + 1 >= len(givenStr) or givenStr[i] != givenStr[i + 1]:
            stringBuilder.append(givenStr[i])
            stringBuilder.append(str(consecutiveCount))
            consecutiveCount = 0
    return "".join(stringBuilder)


input = "abcd"
output = stringCompression(input)
print(f'\nInput: "{input}"')
print(f'Output: "{output}"')
