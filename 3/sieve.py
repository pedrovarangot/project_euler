#!/bin/python3

import sys
import math

def remove_multiples(factors, number):
    nums = []
    for n in factors:
        if n == number or n % number != 0:
            nums.append(n)
    return nums

t = int(input().strip())
for a0 in range(t):
    num = int(input().strip())
    if num < 105:
        factors = range(2, int(num/2) + 1)
    else:
        factors = range(2, int(math.sqrt(num)) + 1)
    sieve = list(factors)
    sieve.append(num)
    for n in sieve:
        sieve = remove_multiples(sieve, n)
#    print(sieve)
    for n in sorted(sieve, reverse=True):
        if num % n == 0:
            print(n)
            break
