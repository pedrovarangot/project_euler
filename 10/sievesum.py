#!/bin/python3

import sys
from array import array
import math

MAX = 1000000
sieve = array('b', [1]*(MAX+1))
sieve[1] = 0
for i in range(2, int(math.sqrt(MAX))):
    if sieve[i] == 1:
        for i in range(i+i, MAX, i):
            sieve[i] = 0

sums = {}
accumsum = 0
for i in range(1, MAX+1):
    if sieve[i] == 1:
        accumsum += i
    sums[i] = accumsum
        
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sums[n])
