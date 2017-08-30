#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 21:24:06 2017

@author: peter
"""

import math

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

#firstprimes = sieve(10001)

def is_prime_power(n):

    sqrtn = math.sqrt(n)
    candidate = 2
    for i in firstprimes:
        if i > sqrtn:
            return False
        if n % i == 0:
            candidate = i
            break
    isit = False
    for i in range(2, int(math.log2(n)) + 1):
        isit = isit or candidate**i == n
    return isit

#primepowers = list(filter(is_prime_power, range(4,10001)))

            
factors_m = {}
def factors(no):
    if no in factors_m.keys():
        return factors_m[no]
        
    #print("factorising {}".format(no))
    if no == 1:
        return [1]
    if no == 2:
        return [2]
    
    i = 2
    factorsl = []
    n = no
    nok = no
    while i <= math.sqrt(n):
        while n % i == 0:
            factorsl.append(i)
            n = n // i
        if n in factors_m.keys():
            new_factors = list(factors_m[n])
            new_factors.extend(factorsl)
            #print("hit cached factors!")
            factors_m[nok] = new_factors
            return factors_m[nok]
        i += 1
    while no % n == 0 and n != 1:
        #print(n)
        factorsl.append(n)
        no = no // n
        
    factors_m[nok] = factorsl
    return factorsl

def is_power_of_primepowers2(n):
    tfactors = factors(n)
    if is_prime_power(n):
        return True
    if len(tfactors) == len(set(tfactors)):
        return True
    for f in set(tfactors):
        if tfactors.count(f) % 2 != 0:
            return False
        
    return True
        
def is_power_of_primepowers(n):
    if n in firstprimes:
        return True
    for pp in reversed(primepowers):
        if n % pp == 0:
            n = n // pp
    return n == 1
        
weirds = set()
MAX = 100
def test2(n):
    global weirds
    items = set()
    weirds = set()
    for i in range(2, n+1):
        last = i
        powers = []
        added = 0
        for j in range(2,n+1):

            last = i**j
            powers.append(last)
            if last in items:
                weirds.add(i)
                pass
            else:
                added += 1
                items.add(last)
        #print(i, added)
        #print(powers)
    return len(items)
        
def test(n):
    items = set()
    total = 0
    for i in range(2, n+1):
        added = 0
        if not is_power_of_primepowers2(i):
            added = n - 1
            total += (n - 1)
        else:
            last = i
    
            for j in range(2,n+1):
                last *= i
                if not last in items:
                    items.add(last)
                    added += 1
        #print(i, added)
    return total + len(items)
