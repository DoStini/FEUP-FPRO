# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:27:11 2019

@author: morei
"""

import math

sum = 0

for k in range(51):
    sum += (math.factorial(4*k) * (1103 + 26390 * k))/(math.factorial(k)**2 * 396 ** (4 * k))
    
pi = round(9801 / (2 * math.sqrt(2) * sum), 8)

print(pi)