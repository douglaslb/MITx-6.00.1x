# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 16:59:00 2019

@author: doohl
"""

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    
x = int(input("enter a number: "))
ans = factorial(x)
print('The factorial of ' + str(x) + ' is ' + str(ans))