#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    substr_freq_map = {}
    n = len(s)
    total_pairs = 0
    
    for i in range(n):
        freq = [0] * 26
        for j in range(i, n):
            freq[ord(s[j]) - ord('a')] += 1
            freq_tuple = tuple(freq)
            if freq_tuple in substr_freq_map:
                total_pairs += substr_freq_map[freq_tuple]
            if freq_tuple in substr_freq_map:
                substr_freq_map[freq_tuple] += 1
            else:
                substr_freq_map[freq_tuple] = 1
    
    return total_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
