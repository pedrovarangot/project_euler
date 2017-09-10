#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 01:18:40 2017

@author: peter
"""


data = {}
def fillup():
    MAX = 10**18-1
    res = 1
    pos = 1
    level = 2
    for v in range(2, (MAX-1) // 2 + 2):
        for _ in range(4):
            
            pos += level
            res += pos
    
        level += 2
        data[(v-1)*2+1] = res % (10**9+7)
    
fillup()


