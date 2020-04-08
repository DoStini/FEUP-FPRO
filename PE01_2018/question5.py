# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:24:55 2019

@author: morei
"""
from math import log, floor, ceil


dec = int(input("Decimal number = "))

exp = ceil(log(dec, 2))
bin_ = ""
for x in range(exp + 1):
    print(exp-x)
    if 2**(exp-x) <= dec:

        dec -= 2**(exp-x)
        bin_ += "1"
    else:
        bin_ += "0"
bin_ = str(int(bin_)) # removes left "0"

len_ = 0
for digit in bin_:
    len_ += 1
if len_ % 3 == 1:
    bin_ = "00" + bin_
    len_ += 2
elif len_ % 3 == 2:
    bin_ = "0" + bin_
    len_ += 1
cicle = 1
oct_ = ""
sum_ = 0
exp = 2

for a in bin_:
    sum_ += int(a)* 2**exp
    if exp == 0:
        exp = 2
        oct_ += str(sum_)
        sum_ = 0
    else:
        exp -= 1
print(oct_)