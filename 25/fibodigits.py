#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 12:34:32 2017

@author: peter
"""

cache = {}
cache[1] = 1


def fibodigits():
    digits = 1
    term = 2
    fp = 1
    fn = 1
    currentdigits = len(str(fn))
    while(currentdigits < 100):
        fn, fp = fn + fp, fn
        currentdigits = len(str(fn))
        term += 1
        if currentdigits > digits:
            cache[currentdigits] = term
            digits += 1
