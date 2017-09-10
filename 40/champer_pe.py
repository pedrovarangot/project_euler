#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 00:13:16 2017

@author: peter
"""

import math
from decimal import *

getcontext().prec = 19
eps = 0.4
def w0(x): # Lambert W function using Newton's method
    x = float(x)
    if x <= 10:
        w = 0
    else:
        w = math.log(x) - math.log(math.log(x))
    while True:
        
        wNew = (x * math.exp(-w) + w*w) / (w + 1)
        if abs(w - wNew) <= eps:
            break
        w = wNew
    return w
def w03(x): # Lambert W function using Newton's method
    if x <= 10:
        w = Decimal(0)
    else:
        w = x.ln() - x.ln().ln()
    x = float(x)
    w = float(w)
    while True:
        
        wNew = (x * math.exp(-w) + w*w) / (w + 1)
        if abs(w - wNew) <= eps:
            break
        w = wNew
    return Decimal(w)

def i(n):
    log10 = math.log(10) #Decimal(10).ln()
    ninth = 1/9. #Decimal(1) / Decimal(9)
    return math.ceil((w0( log10 / 10**(ninth) * (n - ninth))) / log10 + ninth)

def a(n):
    ian = i(n)
    tenian = 10**ian
    leftp = 10**(( (n + (tenian - 10)/Decimal(9)) % ian) - ian + 1)
    rightp = (( Decimal(9)*n + tenian - 1)/(9*ian) - 1).quantize(Decimal(1), rounding=ROUND_CEILING)
    return ((leftp*rightp) % 10).quantize(Decimal(1), rounding=ROUND_FLOOR)

def test():
    t = int(input().strip())
    
    for _ in range(t):
        vs = map(int, input().strip().split())
        tot = 1
        for v in vs:
            #print(v)
            tot *= a(v)
        print(tot)
        
test()