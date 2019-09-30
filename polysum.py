# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:04:12 2019

@author: doohl
"""

import math

def polysum(n, s):
    
    def areaOfPolygon(n, s):
        area = (0.25* n * s**2)/math.tan(math.pi/n)
        return area
    
    def perimeterOfPolygon(n, s):
        perimeter = n*s
        return perimeter
    sum = areaOfPolygon(n, s) + (perimeterOfPolygon(n, s)**2)
    return round(sum, 4)

