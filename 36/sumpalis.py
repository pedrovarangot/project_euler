#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 01:50:52 2017

@author: peter
"""

def baseN(num,b,digits="0123456789"):
    if num == 1:
        return digits[1]
    elif num == 0:
        return ''
    else:
        return digits[num % b] + baseN(num // b, b, digits)
   # return ((num == 0) and digits[0]) or (baseN(num // b, b, digits).lstrip(digits[0]) + )

def ispali_s(n):
    if len(n) % 2 == 0:
        return list(n[:len(n)//2]) == list(reversed(n[len(n)//2:]))
    else:
        return list(n[:len(n)//2]) == list(reversed(n[len(n)//2+1:]))
        
def ispali(n, k):
    return ispali_s(str(n)) and ispali_s(baseN(n, k))

def test(n, k):
    thesum = 0
    for n in range(1, n):
        if ispali(n, k):
            thesum += n
    return thesum