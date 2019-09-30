# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 23:41:27 2019

@author: doohl
"""

#def applyToEach (L, f):
#    for i in range (len (L)):
#        L [i] = f (L [i])
#
#
#testList = [1, -4, 8, -9]
#
#def timesItSelf (a):
#    return abs(a*a)
#
#applyToEach (testList, timesItSelf)
#print(testList)



def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

print(applyEachTo([inc, square, halve, abs], -3))
