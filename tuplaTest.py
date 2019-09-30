# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 00:39:52 2019

@author: doohl
"""

def quotient_and_remainder(x, y):
    q = x//y
    r = x%y
    return (q, r)

(quot, rem) = quotient_and_remainder(2, 2);
print((quot, rem))