# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 16:26:56 2019

@author: doohl
"""

numFibCalls = 0

def fibonacci(n):
    global numFibCalls
    numFibCalls += 1
    if n == 1 or n == 0:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

x = int (input("Digite um número para calcular o fibonacci: "))
ans = fibonacci(x)


print("O fibonacci de "+ str(x) + " é " + str(ans))
print('functions calls', numFibCalls)