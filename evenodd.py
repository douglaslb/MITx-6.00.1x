# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 01:48:59 2019

@author: doohl
"""

x = int (input("digite um número: "))

if x%2 == 0:
    print("");
    print("par")
    if x%3 == 0:
        print("divisivel por 2 e por 3")
    else:
        print("divisivel por 2 e nao por 3")
else:
    print("")
    print("impar")