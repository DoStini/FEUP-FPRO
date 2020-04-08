# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:07:28 2019

@author: morei
"""

def calculator(expr):
    #one operation
    if type(expr) == tuple:
        if expr[1] == "+":
            return calculator(expr[0]) + calculator(expr[2])
        elif expr[1] == "-":
            return calculator(expr[0]) - calculator(expr[2])
        elif expr[1] == "*":
            return calculator(expr[0]) * calculator(expr[2])
    elif type(expr) == int:
        return expr