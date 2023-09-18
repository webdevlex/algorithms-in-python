#!/bin/python3

import math
import os
import random
import re
import sys


def lonelyinteger(a):
    itemCounts = {}
    for num in a:
        if num not in itemCounts:
            itemCounts[num] = 0
        itemCounts[num] += 1
    for key, value in itemCounts.items():
        if value == 1:
            return key


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + "\n")

    fptr.close()
