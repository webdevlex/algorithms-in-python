def algo(binaryString, requests):
    originalString = binaryString
    flippedString = None
    flipped = False

    answers = []
    for request in requests:
        isFlip = len(request) == 4
        if not isFlip:
            idx = int(request.split(":")[1])
            zeroCount = 0
            for i in range(idx + 1):
                if binaryString[i] == "0":
                    zeroCount += 1
            answers.append(zeroCount)
        else:
            if not flippedString:
                length = len(binaryString)
                mask = (1 << length) - 1
                num = int(binaryString, 2)
                value = num ^ mask
                flippedString = format(value, f"0{length}b")

            if not flipped:
                binaryString = flippedString
                flipped = True
            else:
                binaryString = originalString
                flipped = False
    return answers


result = algo("1111010", ["count:4", "count:6", "flip", "count:4", "flip", "count:2"])
print(result)
