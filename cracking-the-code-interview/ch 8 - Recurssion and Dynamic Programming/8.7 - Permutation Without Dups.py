def permutations(str, memo={}):
    if str in memo:
        return memo[str]

    result = []
    if len(str) == 2:
        result.append(str)
        result.append(str[1] + str[0])
    else:
        for i in range(len(str)):
            char = str[i]
            temp = str.replace(char, "")
            allPerms = permutations(temp, memo)
            for perm in allPerms:
                newPerm = char + perm
                result.append(newPerm)
    memo[str] = result
    return memo[str]
