#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 19:40:16 2017

@author: peter
"""

divsums = {}

for i in range(1, 40000):
    divisor = 2
    divsums[i] = 1
    n = i
    while n > 1 and divisor <= int(n/2):
        if divisor > 1 and n % divisor == 0:
            if divisor != n:
                divsums[i] += divisor
        divisor += 1

amisums = 0
for e,s in divsums.items():
    if e < 10001 and e == divsums[s]:
        print(e)
        amisums += e