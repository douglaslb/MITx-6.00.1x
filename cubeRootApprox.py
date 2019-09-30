# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:54:46 2019

@author: doohl
"""

cube = 25
epsilon = 0.0000001
guess = 0.0
increment = 0.000001
num_guesses = 0

while abs(guess**2 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('num_guesses = ', num_guesses)
if abs(guess**2 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)