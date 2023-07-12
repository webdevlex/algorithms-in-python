def binaryToString(num):
    result = []
    while num > 0:
        if len(result) >= 32:
            return "Error"
        num *= 2
        whole = int(num)
        result.append(str(whole))
        num -= whole
    return "".join(result)


num = 0.5
for i in range(32):
    print(binaryToString(num))
    num /= 2
