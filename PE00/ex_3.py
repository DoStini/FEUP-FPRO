# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:19:02 2019

@author: morei
"""

integers = []
reals = []

if integers == [] or reals == []:
    print("")
else:
    counter = 0
    output = ""
    for x in integers:
        output += str(max(x, reals[counter])) + " "
        counter += 1
    print(output)