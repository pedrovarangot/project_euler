#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 22:07:59 2017

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
    if n <= 100000:
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

def isperm(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))

def test(n, k):
    if k == 3:
        __primesless4d = list([p for p in sieve(n) if 1000 <= p < n])
    else:
        __primesless4d = list([p for p in sieve(n) if 10000 <= p < n])

        
    for p1 in __primesless4d:
        for i in range(2,int('9'*(len(str(p1)))) // (k-1),2):
            if len(str(p1 + (k-1)*i)) > len(str(p1)):
                break
            
            if k == 3:
                if isperm(p1, p1 + i) and isperm(p1, p1 + 2*i):
                    if is_prime(p1 + i) and is_prime(p1 + 2*i):
                        print(p1, p1+i, p1+2*i, sep='')
            else:
                if isperm(p1, p1 + i) and isperm(p1, p1 + 2*i) and isperm(p1, p1 + 3*i):
                    if is_prime(p1 + i) and is_prime(p1 + 2*i) and is_prime(p1 + 3*i):
                        print(p1, p1+i, p1+2*i, p1+3*i, sep='')


        