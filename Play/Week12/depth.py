# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 08:41:46 2019

@author: morei
"""

def maximum_depth(l):
    if len(l) == 0:
        return 1
    else:
        max = 0
        for x in l:
            if maximum_depth(x) > max:
                max = maximum_depth(x)
                
        return 1 + max