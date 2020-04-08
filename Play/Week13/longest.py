# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 22:48:34 2020

@author: morei
"""

from string import punctuation as p

def longest(f1):
    with open(f1, "r") as file:
        f1 = file.read()   
    for x in p:
        f1 = f1.replace(x, "") if x != "-" else f1
        
    return sorted(f1.replace("\n", " ").split(), key=lambda x: len(x))[-1]