BITS = 32


def nextNumber(num):
    print(getNext(num))
    print(getPrev(num))


def getNext(num):
    if num == 0:
        return 1

    numCopy = num
    zeros = 0
    ones = 0
    while (numCopy & 1 == 0) and (numCopy != 0):
        zeros += 1
        numCopy >>= 1

    while (numCopy & 1) == 1:
        ones += 1
        numCopy >>= 1

    noLargerNumber = zeros + ones >= BITS
    if noLargerNumber:
        return -1

    p = zeros + ones
    num |= 1 << p
    num &= ~((1 << p) - 1)
    num |= (1 << (ones - 1)) - 1
    return num


def getPrev(num):
    if num == 1:
        return 0

    numCopy = num
    zeros = 0
    ones = 0

    while (numCopy & 1) == 1:
        ones += 1
        numCopy >>= 1

    while (numCopy & 1) == 0 and (numCopy != 0):
        zeros += 1
        numCopy >>= 1

    noSmallerNumber = zeros + ones >= BITS
    if noSmallerNumber or numCopy == 0:
        return -1

    p = zeros + ones
    num ^= 1 << p
    num &= ~((1 << p) - 1)
    num |= ((1 << ones + 1) - 1) << (zeros - 1)
    return num


nextNumber(15)
