class Decoder:
    def __init__(self):
        self.dashes = []
        self.sequence = {}
        self.complete = False

    def process_sample(self, sequence, character):
        if not self.complete:
            self.sequence[sequence] = character
            if character == "-":
                self.dashes.append(sequence)
                if len(self.dashes) > 1:
                    for i in range(1, len(self.dashes)):
                        message = ""
                        start = i - 1
                        end = i
                        firstComplete = True
                        for j in range(self.dashes[start] + 1, self.dashes[end]):
                            if j not in self.sequence:
                                firstComplete = False
                            else:
                                message += self.sequence[j]

                        if firstComplete:
                            print(message)
                            self.complete = True


example1 = [
    [1, "-"],
    [2, "h"],
    [3, "e"],
    [4, "l"],
    [5, "l"],
    [6, "o"],
    [7, "-"],
    [8, "b"],
    [9, "y"],
]

example2 = [
    [1, "-"],
    [2, "h"],
    [3, "e"],
    [5, "-"],
    [6, "b"],
    [7, "y"],
    [8, "e"],
    [9, "-"],
    [4, "y"],
]

example3 = [[1, "-"], [2, "h"], [3, "e"], [4, "y"], [5, "-"], [6, "b"], [7, "-"]]

allExamples = [example1, example2, example3]

for example in allExamples:
    decoder = Decoder()
    for item in example:
        decoder.process_sample(item[0], item[1])
