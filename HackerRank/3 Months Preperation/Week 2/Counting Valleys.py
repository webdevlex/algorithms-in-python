#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    position = 0
    mountains = 0
    vallys = 0
    for step in path:
        if step == "U":
            if position == 0:
                mountains += 1
            position += 1
        else:
            if position == 0:
                vallys += 1
            position -= 1
    return vallys


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + "\n")

    fptr.close()
