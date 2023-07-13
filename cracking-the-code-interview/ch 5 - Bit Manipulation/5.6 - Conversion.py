def conversion(a, b):
    result = 0
    while a != 0 or b != 0:
        if (a & 1) != (b & 1):
            result += 1
        a >>= 1
        b >>= 1

    return result


print(conversion(29, 15))
