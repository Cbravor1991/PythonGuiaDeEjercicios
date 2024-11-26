#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    for length in range(1, len(s)//2 + 1):
        first_num = int(s[:length])
        temp = str(first_num)
        while len(temp) < len(s):
            temp += str(first_num + 1)
            first_num += 1
        if temp == s:
            print(f"YES {int(s[:length])}")
            return
    print("NO")
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
