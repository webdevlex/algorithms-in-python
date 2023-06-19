def solution(stones):
    stones.sort()

    pile1 = 0
    pile2 = sum(stones)
    i = 0
    while pile1 < pile2 and i != (len(stones) - 1):
        pile1 += stones[i]
        pile2 -= stones[i]
        i += 1

    diffBeforeLastIter = abs((pile1 - stones[i - 1]) - (pile2 + stones[i - 1]))
    currentDiff = abs(pile1 - pile2)
    return min(currentDiff, diffBeforeLastIter)


print(solution([15, 20, 3]))
