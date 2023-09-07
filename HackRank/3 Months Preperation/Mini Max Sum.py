#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    total = arr[0]

    minValue = arr[0]
    minIdx = 0

    maxValue = arr[0]
    maxIdx = 0
    for i in range(1, len(arr)):
        total += arr[i]
        if arr[i] < minValue:
            minValue = arr[i]
            minIdx = i

        if arr[i] > maxValue:
            maxValue = arr[i]
            maxIdx = i

    print(total - arr[maxIdx], total - arr[minIdx])


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
