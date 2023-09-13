def maxCount(arr):
    grid = {}
    maxCount = 0

    for item in arr:
        rc = item.split(" ")
        r = int(rc[0]) + 1
        c = int(rc[1]) + 1
        for i in range(1, r):
            for j in range(1, c):
                if (i, j) not in grid:
                    grid[(i, j)] = 0
                grid[(i, j)] += 1
                if grid[(i, j)] > maxCount:
                    maxCount = grid[(i, j)]
    return maxCount


print(maxCount(["1 4", "2 3", "4 1"]))
