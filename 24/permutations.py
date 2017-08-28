#from itertools import permutations
#perms = sorted(permutations('abcdefghijklm', 13))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 19:10:14 2017

@author: peter
"""

import math

alphabet = list("abcdefghijklm")

def coefs(n):
    coefs = []
    for num in range(1,14):
        coefs.append(n % num)
        n = n // num
    return coefs

def perm(n):
    pick = list(alphabet)
    perm = ""
    for n in reversed(coefs(n)):
        perm += pick[n]
        pick.remove(pick[n])
    return perm

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    print(perm(n-1))
   