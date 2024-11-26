#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def isValid(s):
    freq = {}
    
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    freq_values = list(freq.values())
    freq_count = {}
    
    for f in freq_values:
        freq_count[f] = freq_count.get(f, 0) + 1
    
    if len(freq_count) == 1:
        return "YES"
    
    if len(freq_count) == 2:
        keys = list(freq_count.keys())
        if (keys[0] == 1 and freq_count[keys[0]] == 1) or (keys[1] == 1 and freq_count[keys[1]] == 1):
            return "YES"
        if abs(keys[0] - keys[1]) == 1 and min(freq_count[keys[0]], freq_count[keys[1]]) == 1:
            return "YES"
    
    return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
