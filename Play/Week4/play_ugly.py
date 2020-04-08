# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:53:13 2019

@author: morei
"""

def ugly(n):
    for x in [5, 3, 2]:
        while True:
            print(n, x)
            if n == 1:
                return(True)
            elif n/x >= 1 and n%x == 0:
                n /= x
            else:
                break
    return(False)