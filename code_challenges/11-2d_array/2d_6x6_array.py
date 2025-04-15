# Problem: https://www.hackerrank.com/challenges/2d-array/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

MAX_POINTER_MOVEMENTS = 4


def hourglassSum(arr):
    if arr is None or len(arr) != MAX_POINTER_MOVEMENTS + 2:
        return 0

    max_hourglass_sum = 0
    for i in range(MAX_POINTER_MOVEMENTS):
        for j in range(MAX_POINTER_MOVEMENTS):
            top = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            middle = arr[i + 1][j + 1]
            bottom = arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            current_sum = top + middle + bottom
            max_hourglass_sum = max(max_hourglass_sum, current_sum)

    return max_hourglass_sum


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
