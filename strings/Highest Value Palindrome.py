#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    s = list(s)
    changes_needed = [0] * n

    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            s[i] = s[n - i - 1] = max(s[i], s[n - i - 1])
            changes_needed[i] = 1

    total_changes = sum(changes_needed)

    if total_changes > k:
        return "-1"

    remaining_changes = k - total_changes
    for i in range(n // 2):
        if s[i] != '9':
            if changes_needed[i] == 1:
                if remaining_changes >= 1:
                    s[i] = s[n - i - 1] = '9'
                    remaining_changes -= 1
            else:
                if remaining_changes >= 2:
                    s[i] = s[n - i - 1] = '9'
                    remaining_changes -= 2

    if n % 2 == 1 and remaining_changes > 0:
        s[n // 2] = '9'

    return ''.join(s)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
