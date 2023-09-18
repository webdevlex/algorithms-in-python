def algo(n):
    if n == 1:
        return getAlphabet()

    halfN = n // 2
    allHalves = []
    currentHalf = [0] * halfN
    makeHalves(halfN, currentHalf, allHalves)

    allPals = []
    isEven = n % 2 == 0
    makePals(allHalves, allPals, isEven)
    return allPals


def makeHalves(n, currentHalf, allHalves, memo=set()):
    key = "".join([str(x) for x in currentHalf])

    if key not in memo:
        memo.add(key)
        allHalves.append(currentHalf)

        for i in range(len(currentHalf)):
            if currentHalf[i] < 25:
                copy = currentHalf.copy()
                copy[i] += 1
                makeHalves(n, copy, allHalves, memo)


def makePals(allHalves, allPals, isEven):
    for item in allHalves:
        value = "".join([chr(x + 97) for x in item])

        if not isEven:
            alphabet = getAlphabet()
            for char in alphabet:
                allPals.append(value + char + value[::-1])
        else:
            allPals.append(value + value[::-1])


def getAlphabet():
    alphabet = []
    for i in range(26):
        alphabet.append(chr(i + 97))
    return alphabet


print(algo(5))
