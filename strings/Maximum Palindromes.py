#!/bin/python3

import math
import os
import random
import re
import sys

MOD = 1000000007

def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def initialize(s):
    n = len(s)
    prefix_counts = [[0] * 26 for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(26):
            prefix_counts[i][j] = prefix_counts[i - 1][j]
        prefix_counts[i][ord(s[i - 1]) - ord('a')] += 1
    max_factorial = n
    fact = [1] * (max_factorial + 1)
    inv_fact = [1] * (max_factorial + 1)
    for i in range(2, max_factorial + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact[max_factorial] = mod_exp(fact[max_factorial], MOD - 2, MOD)
    for i in range(max_factorial - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    return prefix_counts, fact, inv_fact

def combinations(n, r, fact, inv_fact):
    if n < r or r < 0:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

def answerQuery(l, r, prefix_counts, fact, inv_fact):
    l -= 1
    freq = [prefix_counts[r][i] - prefix_counts[l][i] for i in range(26)]
    pairs = sum(count // 2 for count in freq)
    singles = sum(count % 2 for count in freq)
    arrangements = fact[pairs]
    for count in freq:
        if count // 2 > 0:
            arrangements = arrangements * inv_fact[count // 2] % MOD
    total_palindromes = (arrangements * max(1, singles)) % MOD
    return total_palindromes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    prefix_counts, fact, inv_fact = initialize(s)
    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        l = int(first_multiple_input[0])
        r = int(first_multiple_input[1])
        result = answerQuery(l, r, prefix_counts, fact, inv_fact)
        fptr.write(str(result) + '\n')
    fptr.close()
