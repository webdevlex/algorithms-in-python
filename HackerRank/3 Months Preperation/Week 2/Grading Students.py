import math
import os
import random
import re
import sys


def gradingStudents(grades):
    results = []
    for grade in grades:
        neededForNext5 = 5 - (grade % 5)
        newGrade = grade
        if grade >= 38 and neededForNext5 < 3:
            newGrade += neededForNext5
        results.append(newGrade)

    return results


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
