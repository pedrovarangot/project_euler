#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 19:10:18 2017

@author: peter
"""

def sum_power_digits(n, p):
    sum = 0
    for d in str(n):
        sum += int(d)**p
    return sum


        