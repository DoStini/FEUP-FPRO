# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 09:43:06 2019

@author: morei
"""

lower = int(input())
upper = int(input())
final_string = "Prime numbers between {0} and {1} are: ".format(lower, upper)
for x in range(lower, upper + 1):
    prime = True
    if x == 2:
        final_string += "2 "
        continue
    elif(x < 2):
        continue
    for y in range(2, x):
        if (x % y == 0):
            prime = False
    if prime:
        final_string += str(x) + " "
    
print(final_string)