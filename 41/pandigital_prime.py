#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 20:36:24 2017

@author: peter
"""

from itertools import permutations
import itertools
from functools import reduce
from bisect import bisect_right

# sqrt(9999999999) = 31622

def candidate_range(n):
    cur = 5
    incr = 2
    while cur < n+1:
        yield cur
        cur += incr
        incr ^= 6

def sieve(end):
    prime_list = [2, 3]
    sieve_list = [True] * (end+1)
    for each_number in candidate_range(end):
        if sieve_list[each_number]:
            prime_list.append(each_number)
            for multiple in range(each_number*each_number, end+1, each_number):
                sieve_list[multiple] = False
    return prime_list

__primes = sieve(1000000)
__primes_set = set(__primes)

def is_prime(n):
    # if prime is already in the list, just pick it
    if n <= 1000000:
        return n in __primes_set
    # Divide by each known prime
    limit = int(n ** .5)
    for p in __primes:
        if p > limit: return True
        if n % p == 0: return False
    # fall back on trial division if n > 1 billion
    for f in range(31627, limit, 6): # 31627 is the next prime
        if n % f == 0 or n % (f + 4) == 0:
            return False
    return True

def pandigital_primes(n):
    digits = range(1,n+1)
    for num in permutations(digits, n):
        dnum = reduce(lambda rst, d: rst * 10 + d, num)
        if is_prime(dnum):
            yield dnum
            
_pandigital_primes = sorted(list(itertools.chain.from_iterable(map(pandigital_primes, range(1,9)))))
        
def test(n):
    if _pandigital_primes[bisect_right(_pandigital_primes, n)-1] <= n:
        print(_pandigital_primes[bisect_right(_pandigital_primes, n)-1])
    else:
        print(-1)

