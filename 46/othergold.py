#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 21:27:02 2017

@author: peter
"""

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

__primes = sieve(10**5+1)
__primes_set = set(__primes)

def is_prime(n):
    # if prime is already in the list, just pick it
    if n <= 10**5+1:
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

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def non_other_gold(n):
    if is_prime(n):
        return True
    
    for p in __primes:
        if p > n:
            print(p)
            return False
        
        candidate = n - p
        sqr = isqrt(candidate//2)
        if candidate % 2 == 0 and candidate//2 == sqr**2:
            print(p, sqr)
            return True
    
    return False

def ways_gold(n):
    k = 0
    for p in __primes:
        if p > n:
            return k
        
        candidate = n - p
        sqr = isqrt(candidate//2)
        if candidate % 2 == 0 and candidate//2 == sqr**2:
            k += 1
    
    return False

