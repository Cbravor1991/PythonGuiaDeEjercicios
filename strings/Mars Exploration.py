#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    original_message = "SOS"  # The message that was originally sent.
    changed_count = 0
    
    for i in range(len(s)):
        if s[i] != original_message[i % 3]:  # Check each character against the expected 'SOS' pattern
            changed_count += 1
            
    return changed_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
