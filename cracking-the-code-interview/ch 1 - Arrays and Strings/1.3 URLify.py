def urlify(str, trueLength):
    falseEnd = len(str) - 1
    trueEnd = trueLength - 1

    result = list(str)
    while trueEnd != falseEnd:
        if result[trueEnd] == " ":
            result[falseEnd] = "0"
            result[falseEnd - 1] = "2"
            result[falseEnd - 2] = "%"
            falseEnd -= 3
        else:
            result[falseEnd] = result[trueEnd]
            falseEnd -= 1
        trueEnd -= 1
    return "".join(result)


input = "Hello World!  "
output = urlify(input, 12)
print(f'\nInput: "{input}"')
print(f"Output: {output}")
