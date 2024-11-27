#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'longestSequence' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY a as parameter.
#

def divisor_minimo(stick):
    if stick % 2 == 0:
        return 2
    for i in range(3, int(math.sqrt(stick)) + 1, 2):
        if stick % i == 0:
            return i
    return stick

def longestSequence(a):
    total = 0
    for stick in a:
        total += stick
        while stick !=1:
            divisor = divisor_minimo(stick)
            stick //= divisor
            total += stick
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = longestSequence(a)

    fptr.write(str(result) + '\n')

    fptr.close()
