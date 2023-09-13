def algo(binaryString, requests):
    answers = []
    for request in requests:
        if ":" in request:
            idx = int(request.split(":")[1])
            zeroCount = 0
            for i in range(idx + 1):
                if binaryString[i] == "0":
                    zeroCount += 1
            answers.append(zeroCount)
        else:
            length = len(binaryString)
            mask = 1 << len(binaryString)
            mask -= 1
            num = int(binaryString, 2)
            value = num ^ mask
            binaryString = format(value, f"0{length}b")
    return answers


result = algo("1111010", ["count:4", "count:6", "flip", "count:4", "flip", "count:2"])
print(result)
