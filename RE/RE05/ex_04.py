# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:00:52 2019

@author: morei
"""

def triplet(atuple):
    empty = ()
    for x, a in enumerate(atuple):
        for y, b in enumerate(atuple):
            for z, c in enumerate(atuple):
                if a + b + c == 0 and x != y and x != z and y != z:
                    return((a, b, c))
    return empty