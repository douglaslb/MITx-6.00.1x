# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 00:41:24 2019

@author: doohl
"""

x = 5
ans = 0
intersLeft = x

while (intersLeft != 0):
    ans = ans + x
    intersLeft = intersLeft - 1
print(str(x) + '*' + str(x) + ' = ' + str(ans))