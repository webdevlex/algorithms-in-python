def stackOfBoxes(boxes):
    maxHeight = 0
    for i in range(len(boxes)):
        height = helper(boxes, i)
        maxHeight = max(maxHeight, height)

    return maxHeight


def helper(boxes, bottomIdx):
    bottom = boxes[bottomIdx]
    maxHeight = 0
    for i in range(bottomIdx + 1, len(boxes)):
        if bottom[0] >= boxes[i][0] and bottom[1] >= boxes[i][1]:
            height = helper(boxes, i)
            maxHeight = max(
                maxHeight,
                height,
            )
    maxHeight += bottom[2]
    return maxHeight


boxes = [
    [10, 1, 5],
    [3, 3, 1],
    [2, 2, 2],
]
print(stackOfBoxes(boxes))
