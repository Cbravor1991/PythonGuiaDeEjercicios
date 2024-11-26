#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    freq = [0] * 26

    for char in s:
        freq[ord(char) - ord('a')] += 1

    odd_count = 0
    for count in freq:
        if count % 2 != 0:
            odd_count += 1

    return "YES" if odd_count <= 1 else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
