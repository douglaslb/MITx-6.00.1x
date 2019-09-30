# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 13:08:08 2019

@author: doohl
"""

epsilon = 0.01
numGuesses = 0
low = 0.0
high = 100



print('Please think of a number between 0 and 100!')

while True:
    ans = (high+low)//2.0
    print("Is your secret number", str(ans), "?")
    resp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if resp=='l':
        low = ans
    elif resp=='h':
        high = ans
    elif resp == 'c':
        print('Game over. Your secret number was:', str(ans))
        break
    else:
         print('Sorry, I did not understand your input.')

    

