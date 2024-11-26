#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    missing_digit = missing_lower = missing_upper = missing_special = 0
    
    for char in password:
        if char in numbers:
            missing_digit = 1
        elif char in lower_case:
            missing_lower = 1
        elif char in upper_case:
            missing_upper = 1
        elif char in special_characters:
            missing_special = 1

    missing_types = 4 - (missing_digit + missing_lower + missing_upper + missing_special)
    
    if n < 6:
        return max(missing_types, 6 - n)
    
    return missing_types

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
