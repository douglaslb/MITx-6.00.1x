# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:51:15 2019

@author: doohl
"""

def biggest(aDict): 
    biggestValue = 0
    x = ''
    if bool(aDict) == False:
        return None
    else:
        for key in aDict.keys():
            if len(aDict[key]) >= biggestValue:
                x = key
                biggestValue = len(aDict[key])
        return x

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
animals['e'] = ['chihuahua']