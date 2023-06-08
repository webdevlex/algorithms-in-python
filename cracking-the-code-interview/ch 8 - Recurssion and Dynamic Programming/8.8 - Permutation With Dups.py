def permutationWithDups(strg):
    table = {}
    for char in strg:
        if char not in table:
            table[char] = 1
        else:
            table[char] += 1
    return helper(table)


def helper(table):
    result = []
    for key, value in table.items():
        if value != 0:
            tableCopy = table.copy()
            tableCopy[key] -= 1
            perms = helper(tableCopy)

            if len(perms) == 0:
                result.append(key)
            else:
                for perm in perms:
                    result.append(key + perm)
    return result


print(permutationWithDups("aab"))
