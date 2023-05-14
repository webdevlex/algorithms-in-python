def oneAway(str1, str2):
    str1Length = len(str1)
    str2Length = len(str2)
    if str1Length - 1 == str2Length:
        return oneAwayInsert(str1, str2)
    elif str1Length == str2Length - 1:
        return oneAwayInsert(str2, str1)
    elif str1Length == str2Length:
        return oneAwayReplace(str1, str2)
    return False


def oneAwayInsert(str1, str2):
    idx1 = 0
    idx2 = 0
    lastIdx = len(str1)
    while idx1 < lastIdx:
        if str1[idx1] != str2[idx2]:
            if idx1 != idx2:
                return False
            idx1 += 1
        else:
            idx1 += 1
            idx2 += 1

    return True


def oneAwayReplace(str1, str2):
    mismatchFound = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if mismatchFound:
                return False
            mismatchFound = True
    return True


input1 = ""
input2 = "pale"
output = oneAway(input1, input2)
print(f'\nInput: "{input1}", "{input2}"')
print(f"Output: {output}")
