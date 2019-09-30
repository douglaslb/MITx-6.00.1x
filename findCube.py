# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 12:01:57 2019

@author: doohl
"""

#x = int(input("Digite um número inteiro: "))
#ans = 0
#
#while n  < abs(x):
#    ans = ans + 1
#if ans**2 != abs(x):
#    print(str(x) + ' não é uma raiz perfeita')
#else:
#    if x < 0:
#        print('Raiz quadrada de ' + str(x) + ' é ' + str(ans))

cube = 9
for guess in range(abs(cube+1)):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, "não é uma raiz perfeita")
else: 
    if cube<0:
        guess = -guess
    print ("Raiz cubica de ", cube, " é ", guess)
