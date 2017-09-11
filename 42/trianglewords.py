#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 20:03:28 2017

@author: peter
"""

import math

sumword = lambda w: sum(map(lambda s: ord(s) - 64, w))

def istriangle(num):
    
    
    
    if num == 2:
        return (False, 0)
    else:
        twicenum = 2*num
        numsqrt = math.sqrt(twicenum)
        if math.floor(numsqrt) == numsqrt: return (False, 0)
        return (math.floor(numsqrt) * math.ceil(numsqrt) == twicenum, math.floor(numsqrt))

def test_pe():
    f = open('p042_words.txt')
    
    sumwords = 0
    for line in f:
        words = line.split(',')
        for word in words:
            if istriangle(sumword(word[1:len(word)-1])):
                print(sumword(word[1:len(word)-1]))
                sumwords += 1
                
def test_epp():
    k = int(input().strip())
    for _ in range(k):
        n = int(input().strip())
        test_triangle = istriangle(n)[1]
        if test_triangle[0]:
            print(test_triangle[1])
        else:
            print(-1)