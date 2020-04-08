# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 13:10:26 2020

@author: morei
"""

def compatible(A,B):
    try:
        assert len(A[0]) == len(B), 'A and B cannot be multiplied'
    except AssertionError as error:
        return error
    else:    
        return "A and B can be multiplied"