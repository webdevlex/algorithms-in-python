def adRotation(num):
    numBits = len(bin(num)[2:])
    mask = 1 << (numBits)
    mask -= 1
    return num ^ mask


value = 30
print("original:", format(value, "08b"))
print("result:", format(adRotation(value), "08b"))
