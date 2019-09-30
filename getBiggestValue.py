# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:51:15 2019

@author: doohl
"""


def how_many(aDict):
    count = 0
    for x in aDict.values(): 
        count += len(x)
    return count 
        

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}
animals.values()

