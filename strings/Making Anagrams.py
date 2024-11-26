#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def makingAnagrams(s1, s2):
    freq1 = [0] * 26
    freq2 = [0] * 26

    for char in s1:
        freq1[ord(char) - ord('a')] += 1

    for char in s2:
        freq2[ord(char) - ord('a')] += 1

    deletions = 0
    for i in range(26):
        deletions += abs(freq1[i] - freq2[i])

    return deletions
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
