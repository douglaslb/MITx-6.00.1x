# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 17:53:34 2019

@author: doohl
"""

def printMove(fr, to):
    print('move from ' + str(fr)+ ' to ' + str(to))
    
def Towers(n, fr, to, spare):
    if n == 1:
        return printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
print(Towers(4, "P1", "P2", "P3"))