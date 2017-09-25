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

def factorsno(n):
    return len(set(factors(n)))

def test():
    upto = 10000000000
    candidates = zip(range(647, upto), range(648, upto), range(649, upto), range(650, upto))
    for candidate in candidates:
        isit = True
        for num in candidate:
            isit = isit and factorsno(num) == 4
            if not isit:
                break
        if isit:
            print(candidate[0])


