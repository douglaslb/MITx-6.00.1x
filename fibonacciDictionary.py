# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 17:19:34 2019

@author: doohl
"""

def fib_efficient(n, d):
    global numFibCalls
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans

numFibCalls = 0

d = {1:1, 2:2}
print(fib_efficient(34, d))
print('functions calls', numFibCalls)