# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:20:05 2019

@author: morei
"""

def roman_to_integer(astring):
    dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M": 1000}
    idx = 0
    total  = 0 
    while idx < len(astring):
        if idx + 1 < len(astring):
            if dic[astring[idx]] >= dic[astring[idx + 1]]:
                total += dic[astring[idx]]
            else:
                total -= dic[astring[idx]]
        else:
            total += dic[astring[idx]]
        idx += 1
    return total