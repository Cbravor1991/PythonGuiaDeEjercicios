#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        #busca en los valores corchete de apertura que esta en el valor
        if char in bracket_map.values():
            stack.append(char)
        #ve que si no es un corvhete de aprtura es un cochete de cieere
        elif char in bracket_map.keys():
            #verifica que la pila no este vacia y que el ultimo valor agregado coincida con el 
            #valor de apertura para el corchete de cieere obtenido que es bracket_map[char]
            if not stack or stack[-1] != bracket_map[char]:
                return "NO"
            stack.pop()
    
    return "YES" if not stack else "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
