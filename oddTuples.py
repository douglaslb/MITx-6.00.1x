# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 01:05:39 2019

@author: doohl
"""

def oddTuples(aTup):
    newTup = ()
    
    for i in range(len(aTup)):
        if(i%2==0):
            newTup = newTup + (aTup[i], )
    return (newTup)


(oddTuple) = oddTuples(('I', 'am', 'a', 'test', 'tuple'))