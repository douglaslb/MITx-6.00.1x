# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:29:22 2019

@author: doohl
"""
num = 11
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''

while num > 0:
    result = str(num%2) + result
    num = num//2
if isNeg:
    result = ' - ' + result