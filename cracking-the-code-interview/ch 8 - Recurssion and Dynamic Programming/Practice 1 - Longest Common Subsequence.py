# ----- Recursive -----
# def lcs(str1, str2, i=0, j=0):
#     if i >= len(str1) or j >= len(str2):
#         return 0
#     elif str1[i] == str2[j]:
#         return 1 + lcs(str1, str2, i+1, j+1)
#     else:
#         return max(lcs(str1, str2, i+1, j), lcs(str1, str2, i, j+1))

# ----- Memoization -----
# def lcs(str1, str2):
#     memo = [[-1] * len(str2)] * len(str1)
#     print(memo)
#     return lcsHelper(str1, str2, 0, 0, memo)

# def lcsHelper(str1, str2, i, j, memo):
#     if i >= len(str1) or j >= len(str2):
#         return 0
#     elif memo[i][j] != -1:
#         return memo[i][j]
#     elif str1[i] == str2[j]:
#         memo[i][j] = 1 + lcsHelper(str1, str2, i+1, j+1, memo)
#         return memo[i][j]
#     else:
#         memo[i][j] =  max(lcsHelper(str1, str2, i+1, j, memo), lcsHelper(str1, str2, i, j+1, memo))
#         return memo[i][j]


# ----- Tabulation -----
# def lcs(str1, str2):
#     lenOfStr1 = len(str1)
#     lenOfStr2 = len(str2)
#     table = createTable(lenOfStr1 + 1, lenOfStr2 + 1)

#     for i in range(1, lenOfStr1 + 1):
#         for j in range(1, lenOfStr2 + 1):
#             if str1[i - 1] == str2[j - 1]:
#                 table[i][j] = 1 + table[i - 1][j - 1]
#             else:
#                 table[i][j] = max(table[i - 1][j], table[i][j - 1])
#     return table[lenOfStr1][lenOfStr2]


# def createTable(rows, columns):
#     table = []

#     for i in range(rows):
#         row = [-1] * columns
#         row[0] = 0
#         table.append(row)

#     for j in range(columns):
#         table[0][j] = 0

#     return table


print(lcs("abcde", "ace"))
