#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 19:40:16 2017

@author: peter
"""


import math
from itertools import combinations
from array import array

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

def divisors_less_than(n):
    if n == 1:
        return [1]
    factors_list = list(factors(n))
    if n in factors_list:
        factors_list.remove(n)
    factors_list.append(1)
    rv = set()
    for i in range(len(factors_list)):
        for divisor_factors in combinations(factors_list, i):
            divisor = 1
            for factor in divisor_factors:
                divisor *= factor
            if divisor != n:
                rv.add(divisor)
    return rv

amisums_m = array('I',  [0] * 100000)
max_n = 1

def test(n):
    global max_n
    if n < max_n:
        return amisums_m[n]
    amisums = amisums_m[max_n]
    for i in range(max_n, n):
        sd1 = sum(divisors_less_than(i))
        if sd1 != i and i == sum(divisors_less_than(sd1)):
            #print(sd1)
            amisums += i
        amisums_m[i] = amisums
        max_n = i
    return amisums
