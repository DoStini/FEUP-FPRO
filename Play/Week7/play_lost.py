# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 08:56:31 2019

@author: morei
"""

def lost_element(s1, s2):
    for a in s1 ^ s2:
        return a