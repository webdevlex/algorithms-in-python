#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    pos = 0
    zero = 0
    neg = 0
    for num in arr:
        if num > 0:
            pos += 1
        elif num == 0:
            zero += 1
        else:
            neg += 1
    print(format(round(pos / len(arr), 6), ".6f"))
    print(format(round(neg / len(arr), 6), ".6f"))
    print(format(round(zero / len(arr), 6), ".6f"))


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
