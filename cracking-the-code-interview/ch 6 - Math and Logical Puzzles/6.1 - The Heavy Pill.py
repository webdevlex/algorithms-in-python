def theHeavyPill(numBottles):
    sumWithoutHeavy = 0
    for i in range(1, numBottles + 1):
        sumWithoutHeavy += i

    for i in range(1, numBottles + 1):
        print(f"If weight is {sumWithoutHeavy + (0.1 * i)} then heavy is bottle {i}")


theHeavyPill(20)
