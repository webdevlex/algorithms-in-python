# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput


def camelCase(line):
    operation = line[0]
    lineType = line[2:3]
    name = line[4:]

    if operation == "S":
        if lineType == "M":
            name = name[:-2]

        uppers = []
        for i in range(len(name)):
            if name[i].isupper():
                uppers.append(i)

        result = name[: uppers[0]]
        if uppers[0] != 0:
            result += " "

        for i in range(len(uppers) - 1):
            result += name[uppers[i] : uppers[i + 1]].lower()
            result += " "
        result += name[uppers[-1] :].lower()

        print(result)

    else:
        words = name.split(" ")

        result = ""
        if lineType == "C":
            result += words[0].capitalize()
        else:
            result += words[0]

        for i in range(1, len(words)):
            result += words[i].capitalize()

        if lineType == "M":
            result += "()"
        print(result)


for line in fileinput.input():
    camelCase(line.rstrip())
