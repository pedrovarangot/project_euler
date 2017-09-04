#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 23:16:55 2017

@author: peter
"""

MAX = 10
ways_change_d = [[{}]] * (MAX + 1)
ways_change_d[1] = [{1:1}]

ways_change = [0] * (MAX + 1)
ways_change[1] = 1
ways_change[2] = 2

coins = [200, 100, 50, 20, 10, 5, 2, 1]

def expensive_sol():
    for i in range(2, MAX + 1):
        new_ways = []
        for coin in coins:
            
            if i - coin >= 0:
                old_ways = ways_change[i-coin].copy()
                for way in old_ways:
                    reway = way.copy()
                    reway[coin] = reway.get(coin, 0) + 1
                    if reway not in new_ways:
                        new_ways.append(reway)
        ways_change[i] = new_ways
                
def optimal_sol():
    for i in range(3, MAX + 1):
        available_coins = [c for c in coins if c < i]
        largest_coin = available_coins[0]
        
        target_i = i - largest_coin
        ways_change[i] += ways_change[target_i] + 1
            
        if i in coins:
            ways_change[i] += 1
                
        
            



