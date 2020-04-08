# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:03:05 2019

@author: morei
"""

from string import ascii_lowercase

def complete_pairs(s1, s2):
    output = set({})
    alpha = set(ascii_lowercase)
    for a in s1:
        for b in s2:
            if set(a)|set(b) == alpha:
                output.add(a + b)
    return output