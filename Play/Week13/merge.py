# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 22:16:15 2020

@author: morei
"""

def interleave(f1, f2):
    with open(f1, "r") as file:
        f1 = file.read().split("\n")
    with open(f2,"r") as file:
        f2 = file.read().split("\n")
    
    out = ""
    min_ = min((len(f1), len(f2)))
    for x in range(min_):
        out += f1[x] + "\n" + f2[x] + "\n" if x != len(f1)-1 else f1[x] + f2[x]
        
    return out