# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:05:43 2019

@author: morei
"""

n = int(input())
result = ""
for x in range(1, n + 1):
    mult_3 = (x%3 == 0)
    mult_5 = (x%5 == 0)
    if (mult_3 and mult_5):
        pass
    elif(mult_3):
        result += "Fizz "
    elif(mult_5):
        result += "Buzz "
    else:
        result += str(x) + " "
    
print (result)