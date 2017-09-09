#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 10:50:15 2017

@author: peter
"""

import itertools

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

__primes = sieve(10**6+1)
MAXP = 10**6
__primesless1m = list([p for p in __primes if 2 <= p <= MAXP])

__primes_set = set(__primes)

def is_prime(n):
    # if prime is already in the list, just pick it
    if n <= 1000000:
        return n in __primes_set
    # Divide by each known prime
    limit = int(n ** .5)
    for p in __primes:
        if p > limit: return True
        if n % p == 0: return False
    # fall back on trial division if n > 1 billion
    for f in range(31627, limit, 6): # 31627 is the next prime
        if n % f == 0 or n % (f + 4) == 0:
            return False
    return True

def test():
    results = []
    primen = 1
    currentbound = 1
    for p in __primesless1m:
    
        
        lastprime = 2
        maxprimesum = 0
        
        take = 0
        while True:
            thisprimes = __primes[take:]
            if primen - take < currentbound:
                break
            if p - thisprimes[0] < thisprimes[currentbound - 1]:
                break
            if p - sum(thisprimes[:currentbound]) < 0:
                break
            primesupto = iter(thisprimes)
            candidate = p
            primesinsum = 0
    
            while candidate > 0:
                
                lastprime = next(primesupto)
                candidate -= lastprime
                #print(p, candidate, lastprime)
                primesinsum += 1
            if candidate == 0 and primesinsum > maxprimesum:
                maxprimesum = primesinsum
                print(p, primesinsum, __primes[take:][0])
                results.append((p, primesinsum, __primes[take:][0]))
                if primesinsum > currentbound:
                    currentbound = primesinsum
            take += 1
        primen += 1


def test2():
    removel = 0
    remover = 0
    q = [(removel, remover)]
    
    while q != []:
        #print(len(q))
        elem, *q = q
        
        current = sum(__primesless1m[elem[0]:len(__primesless1m) - elem[1]])
        if current <= 1000000 and is_prime(current):
            print(elem)
            print(current)
            
        swapl = removel
        swapr = remover
        if removel < MAXP:
            removel += 1
            q.append((removel, remover))
        if remover < MAXP:
            remover += 1
            q.append((removel, remover))
        if removel != swapl:
            q.append((swapl, remover))
    
def is_prime2(n):
    if n<=1:
        return False
    elif n<=3:
        return True
    elif n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i = i+6
    return True

def find_next_prime(n):
    while True:
        if is_prime2(n+1):
            return n+1
        else:
            n+=1

def find_longest_sum(n):
    primes = [1,2,3,5,7,11,13]
    primesum = sum(primes)
    best = 0
    bestlen = 0
    while True:
        while primesum <= n:
            #print primes, sum(primes), is_prime(sum(primes)), len(primes)
            if is_prime2(primesum) and len(primes)> bestlen:
                best = primesum
                bestlen = len(primes)
            primes.append(find_next_prime(primes[-1]))
            primesum = sum(primes)
        #print primes, sum(primes), is_prime(sum(primes)), len(primes)
        if is_prime(primesum) and len(primes) < bestlen:
            return best
        primes = primes[1:-1]
        primesum = sum(primes)

