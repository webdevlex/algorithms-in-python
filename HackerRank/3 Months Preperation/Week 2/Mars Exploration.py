#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def marsExploration(s):
    numMessages = len(s) // 3
    numErrors = 0
    for i in range(numMessages):
        firstIdx = i * 3
        secondIdx = (i * 3) + 1
        thirdIdx = (i * 3) + 2
        if s[firstIdx] != "S":
            numErrors += 1
        if s[secondIdx] != "O":
            numErrors += 1
        if s[thirdIdx] != "S":
            numErrors += 1
    return numErrors


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + "\n")

    fptr.close()
