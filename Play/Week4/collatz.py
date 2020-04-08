# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 09:04:24 2019

@author: morei
"""

def collatz(n):
    prev = n
    string = ""
    if n != 1:
        string += str(n) + ","
    else:
        string += str(n)
    while n != 1:
        if prev % 2 == 0:
            n = prev / 2
            prev = n
        else:
            n = prev * 3 + 1
            prev = n
        n = int(n)
        if n != 1:
            string += str(n) + ","
        else:
            string += str(n)
    return string