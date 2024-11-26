#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def is_palindrome(sub):
        return sub == sub[::-1]

def palindromeIndex(s):
      
    n = len(s)
    left, right = 0, n - 1
    
    while left < right:
        if s[left] != s[right]:
            if is_palindrome(s[left + 1:right + 1]):
                return left
            elif is_palindrome(s[left:right]):
                return right
            else:
                return -1
        left += 1
        right -= 1
    
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
