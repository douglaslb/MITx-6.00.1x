# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 16:06:08 2019

@author: doohl
"""

epsilon = 0.01
y = 54.0
guess = y/2.0
numGuesses = 0


while(guess*guess-y) > epsilon:
    numGuesses += 1
    guess = guess - (((guess**2)-y)/(2*guess))
print('numGuesses = ' + str(numGuesses))
print('Raiz quadrada de ' + str(y) + ' é aproximadamente ' + str(guess))