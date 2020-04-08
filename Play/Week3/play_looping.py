# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 10:14:14 2019

@author: morei
"""

n = int(input())

n = list(str(n))
loop = True
for x in range(0, len(n) - 1):
    if not (abs(int(n[x + 1]) - int(n[x])) == 1 or abs(int(n[x + 1]) - int(n[x])) == 9):
        loop = False
if not loop:
     print("Not a looping number")
else:
     print("Looping number")
