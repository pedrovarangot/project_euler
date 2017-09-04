#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 20:13:25 2017

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

def truncateds(n):
    strn = str(n)
    loops = len(strn)
    while loops > 1:
        strn = strn[:-1]
        loops -= 1
        yield int(strn)
    strn = str(n)   
    loops = len(strn)
    while loops > 1:
        strn = strn[1:]
        loops -= 1
        yield int(strn)


def test(n):
    primes = set(sieve(n))
    sum = 0
    for p in primes:
        if all(map(lambda p: p in primes, truncateds(p))):
            if p not in [2,3,5,7t]:
                sum += p
    print(sum)