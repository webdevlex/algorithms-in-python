def flipBitToWin(num):
    binNum = str(bin(num))[2:]
    oneCounts = []
    currentCount = 0
    for digit in binNum:
        if digit == "0":
            oneCounts.append(currentCount)
            currentCount = 0
        else:
            currentCount += 1
    oneCounts.append(currentCount)

    largestConsecutiveCount = 0
    for i in range(len(oneCounts) - 1):
        currentConsecutiveCount = oneCounts[i] + oneCounts[i + 1]
        if currentConsecutiveCount >= largestConsecutiveCount:
            largestConsecutiveCount = currentConsecutiveCount

    return largestConsecutiveCount + 1


print(flipBitToWin(1770))
