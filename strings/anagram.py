#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    if len(s) % 2 != 0:
        return -1
    
    mid = len(s) // 2
    s1, s2 = s[:mid], s[mid:]
    count = {}
    
    for char in s1:
        count[char] = count.get(char, 0) + 1
    
    for char in s2:
        if char in count and count[char] > 0:
            count[char] -= 1
    
    return sum(count.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
