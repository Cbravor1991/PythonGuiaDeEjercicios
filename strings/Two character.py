#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    max_length = 0
    unique_chars = set(s)

    for char1 in unique_chars:
        for char2 in unique_chars:
            if char1 != char2:
                filtered_string = [char for char in s if char == char1 or char == char2]
                valid = True
                for i in range(len(filtered_string) - 1):
                    if filtered_string[i] == filtered_string[i + 1]:
                        valid = False
                        break
                if valid:
                    max_length = max(max_length, len(filtered_string))
    
    return max_length
    
    return max_length
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
