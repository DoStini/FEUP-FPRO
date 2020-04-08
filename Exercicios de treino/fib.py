# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 18:23:33 2019

@author: morei
"""


def fib(x):
    if x == 1:
        return 1
    if x == 2:
        return 1
    else:
        return fib(x-1) + fib(x-2)