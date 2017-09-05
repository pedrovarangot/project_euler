#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 23:16:55 2017

@author: peter
"""

from collections import OrderedDict

MAX = 200
ways_change_d = [[{}]] * (MAX + 1)
ways_change_d[1] = [{1:1}]

coins_u = {200:7, 100:6, 50:5, 20:4, 10:3, 5:2, 2:1, 1:0}
coins = OrderedDict(sorted(coins_u.items(), key=lambda t: t[0]))

ways_change = [[0 for v in range(MAX + 2)] for c in range(len(coins.keys()))]

def expensive_sol():
    for i in range(2, MAX + 1):
        new_ways = []
        for coin in coins.keys():
            
            if i - coin >= 0:
                old_ways = ways_change_d[i-coin].copy()
                for way in old_ways:
                    reway = way.copy()
                    reway[coin] = reway.get(coin, 0) + 1
                    if reway not in new_ways:
                        new_ways.append(reway)
        ways_change_d[i] = new_ways
                
def optimal_sol():
    for v in range(MAX+1):
        ways_change[0][v] = 1
    for c in range(len(coins.keys())):
        ways_change[c][0] = 1
    
    coins_without_one = [c for c in coins.keys() if c != 1]
    for c in coins_without_one:
        for v in range(MAX+1):
            with_lower_coins = ways_change[coins_u[c] - 1][v]
            if v - c >= 0:
                ways_change[coins_u[c]][v] = with_lower_coins + ways_change[coins_u[c]][v - c]
            else:
                ways_change[coins_u[c]][v] = with_lower_coins

                
        
            
                
        
            



