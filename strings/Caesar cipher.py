#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    encrypted_string = []
    
    for char in s:
        if char.islower():
            encrypted_char = chr(((ord(char) - ord('a') + k) % 26) + ord('a'))
            encrypted_string.append(encrypted_char)
        elif char.isupper():
            encrypted_char = chr(((ord(char) - ord('A') + k) % 26) + ord('A'))
            encrypted_string.append(encrypted_char)
        else:
            encrypted_string.append(char)
    
    return ''.join(encrypted_string)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
