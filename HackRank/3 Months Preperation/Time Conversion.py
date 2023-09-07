#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    hour = int(s[:2])
    minute = s[3:5]
    seconds = s[6:8]
    timeOfDay = s[-2:]
    if timeOfDay == "AM":
        if hour == 12:
            return "00:" + minute + ":" + seconds
        return s[:2] + ":" + minute + ":" + seconds
    else:
        if hour == 12:
            return "12:" + minute + ":" + seconds
        return str(hour + 12) + ":" + minute + ":" + seconds


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = timeConversion(s)

    fptr.write(result + "\n")

    fptr.close()
