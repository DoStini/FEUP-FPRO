# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:40:24 2019

@author: morei
"""

from math import sqrt


def caesar(message):
    alpha = ["a","b","c","d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    out = ""
    for x in range(len(message)):
        if message[x].lower() in alpha:
            fib = int(((1+sqrt(5))**x - (1-sqrt(5))**x) / (2**x * sqrt(5)))
            print(fib)
            shift = alpha.index(message[x].lower()) - fib
            index = int(shift%26)
            out += alpha[index].upper()
        else:
            out += message[x]
    return(out)        
print(caesar("HELLO WORLD!"))