#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 12:20:28 2017

@author: peter
"""

from array import array

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

def order(n, p):
    i = 1
    while pow(n,i,p) != 1:
        i += 1
    return i

MAX = 10001

maxd = array('I', [0] * (MAX))
orders = list(map(lambda n: (order(10, n), n), sieve(MAX)[3:]))

maxtup = (1,3)
for i in range(MAX):
    if len(orders) > 0 and orders[0][1] < i:
        if orders[0][0] > maxtup[0]:
            maxtup, *orders = orders
        else:
            orders = orders[1:]
    maxd[i] = maxtup[1]
        
def test(n):
    return maxd[n]
        
    