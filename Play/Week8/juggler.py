# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 11:50:33 2019

@author: morei
"""

import math

def juggler(n, p):
    if p == 0:
        return n
    else:
        val = juggler(n, p-1)
        if val % 2 == 0:
            return math.floor(math.sqrt(val))
        else:
            return math.floor(math.sqrt(val**3))