#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 20:41:43 2017

@author: peter
"""

def digits(n):

    digit = lambda c: ord(c) - 48

    return sorted(map(digit, str(n)))


def test(n,k):
    thedigits = set([1,2,4,5,7,8])
    for i in range(1, n+1):
        ndigits = digits(i)
        if 6 in ndigits:
            continue
        if not set(ndigits).issuperset(thedigits):
            continue
        isit = True
        nums = [i]
        for j in range(2,k+1):
            isit = isit and (ndigits == digits(j*i))
            if not isit:
                break
            nums.append(j*i)
        if isit:
            print(*nums, sep=' ')

