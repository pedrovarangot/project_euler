#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 11:55:37 2017

@author: peter
"""

import itertools
import math
from decimal import *

def nines(n):
    numbernines = 0
    
    while numbernines < n:
        numbernines += 1
        yield int('9' * numbernines)

def tester(n):
    for i in range(1, n):
        yield str(i)

def test2(n):
    return int(list(itertools.chain(*tester(int(str('9'*len(str(n)))))))[n-1])

eps = Decimal(0.000000001)
def w0(x): # Lambert W function using Newton's method
    if x <= 10:
        w = Decimal(0)
    else:
        w = x.ln() - x.ln().ln()
    while True:
        
        wNew = (x * (-w).exp() + w*w) / (w + 1)
        if abs(w - wNew) <= eps:
            break
        w = wNew
    return w

def i(n):
    log10 = Decimal(10).ln()
    ninth = Decimal(1) / Decimal(9)
    return (w0( log10 / 10**(ninth) * (n - ninth)) / log10 + ninth).quantize(Decimal(1), rounding=ROUND_CEILING)

def a(n):
    ian = i(n)
    leftp = 10**(( (n + (10**ian - 10)/Decimal(9)) % ian) - ian + 1)
    rightp = (( Decimal(9)*n + 10**ian - 1)/(9*ian) - 1).quantize(Decimal(1), rounding=ROUND_CEILING)
    return ((leftp*rightp) % 10).quantize(Decimal(1), rounding=ROUND_FLOOR)

def testF(n):
    niness = nines(9)
    if n < 10:
        return n
    if n == 10:
        return 1
    next(niness)
    
    position = 10
    while position < n:
        number_of_numbers = next(niness)
        if position + number_of_numbers * len(str(number_of_numbers)) < n:
            position += number_of_numbers * len(str(number_of_numbers))
            continue
        else:
            for p in range(position, number_of_numbers * len(str(number_of_numbers))):
                if position + len(str(p)) < n:
                    position += len(str(p))

                else:
                    return int(str(p)[n-position])
                    break
            break
    
    print(position)
