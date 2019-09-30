# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 13:08:08 2019

@author: doohl
"""

x = 54
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' hight = ' + str(high) + ' ans =  ' +str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ', numGuesses)
print('A raiz quadrada de', x, ' é aproximadamente', ans) 