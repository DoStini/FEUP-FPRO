# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 11:54:54 2019

@author: morei
"""

def adigits(n1, n2, n3):
    n_1 = int(n1+n2+n3)
    n_2 = int(n1+n3+n2)
    n_3 = int(n2+n1+n3)
    n_4 = int(n2+n3+n1)
    n_5 = int(n3+n1+n2)
    n_6 = int(n3+n2+n1)
    
    return(max(n_1, n_2, n_3, n_4, n_5, n_6))
    
print(adigits("9", "1", "9"))