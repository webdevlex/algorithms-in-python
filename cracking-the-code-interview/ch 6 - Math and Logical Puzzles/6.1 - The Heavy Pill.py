# Question: You have 20 bottles of pills. 19 bottles have 1.0 gram pills, but one has pills of weight
# 1.1 grams. Given a scale that provides an exact measurement, how would you find the heavy bottle?
# You can only use the scale once.


def theHeavyPill(numBottles):
    sumWithoutHeavy = 0
    for i in range(1, numBottles + 1):
        sumWithoutHeavy += i

    for i in range(1, numBottles + 1):
        print(f"If weight is {sumWithoutHeavy + (0.1 * i)} then heavy is bottle {i}")


theHeavyPill(20)
