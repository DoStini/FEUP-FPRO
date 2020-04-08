# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 15:52:46 2019

@author: morei
"""

dec = int(input())
bin_ = ""

while True:
    if (dec == 0):
        break
    bit = dec % 2
    dec = int(dec/2)
    bin_ += str(bit)
binary = ""
for x in range(0, len(bin_)):
    binary += bin_[len(bin_) - 1 - x]    

print(binary)