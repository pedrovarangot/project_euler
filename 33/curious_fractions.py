#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 18:41:20 2017

@author: peter
"""

from math import gcd
from itertools import permutations

def lowest_terms(n,d):
    gcdv = gcd(d,n)
    return (n//gcdv, d//gcdv)

def curious_candidate(n,d,k):
    if n == d:
        return False
    ndigits = str(n)
    ddigits = str(d)
    for digit in ndigits:
        if digit in ddigits and digit != '0':
            if k == 1:
                return True
            else:
                k -= 1

    return False

def curious_digits(n,d):
    ndigits = str(n)
    ddigits = str(d)
    
    for digit in ndigits:
        if digit in ddigits and digit != "0":
            
            yield digit

def simplify_curious(n, d, k):
    #print(n,d)
    
    tosimplify = permutations(curious_digits(n,d), k)
    strn = str(n)
    strd = str(d)
    
    positionsn = []
    positionsd = []
    for digits in tosimplify:
        for digit in digits:
            position = strn.find(digit)
            while position != -1:
                positionsn.append(position)
                position = strn.find(digit, position+1)
            
            position = strd.find(digit)
            while position != -1:
                positionsd.append(position)
                position = strd.find(digit, position+1)
                
    # This should use permutations of shorter list and not always same order
    if len(positionsn) > len(positionsd):
        positionsd = positionsd * (len(positionsn) // len(positionsd))
    elif len(positionsn) < len(positionsd):
        positionsn = positionsn * (len(positionsd) // len(positionsn))
    
    #print(positionsn, positionsd)
    simplified = set()
    while len(positionsn) > 0:
        nsubs, positionsn = positionsn[:k], positionsn[k:]
        dsubs, positionsd = positionsd[:k], positionsd[k:]
        
        strn_simplified = list(strn)
        strd_simplified = list(strd)
        for digit in nsubs:
            strn_simplified[digit] = None
        for digit in dsubs:
            strd_simplified[digit] = None
            
        if all(map(lambda a: a == None or a == '0', strn_simplified)):
            continue
        if all(map(lambda a: a == None or a == '0', strd_simplified)):
            continue
        #print(strn_simplified, strd_simplified)
        
        simplified.add((int(''.join([d for d in strn_simplified if d is not None])),
               int(''.join([d for d in strd_simplified if d is not None]))))
    return simplified

maxnum = {2:100, 3:1000, 4:10000}

def test(num,k):
    sumn = 0
    sumd = 0
    for d in range(1, maxnum[num]):
        for n in range(1, d):
            if curious_candidate(n,d,k):
                #print(n,d)
                lowest_termsf = lowest_terms(n,d)
                posibilities = simplify_curious(n,d,k)
                for posibility in posibilities:
                    if lowest_terms(*posibility) == lowest_termsf:
                        sumd += d
                        sumn += n
    if sumn != 0 and sumd != 0:
        print(sumn, sumd)
        

                


