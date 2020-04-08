# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:12:03 2019

@author: morei
"""

tS = float(input("Swimming stage time: "))
tC = float(input("Cycling stage time: "))
tR = float(input("Running stage time: "))

time = tS + tC + tR

vS = 1.5 / tS
vC = 40 / tC
vR = 10 / tR

if time >= 4:
    print("Time")
elif vS < 2:
    print("Swimming")
elif vC < 20:
    print("Cycling")
elif vR < 8:
    print("Running")
else:
    print(time)