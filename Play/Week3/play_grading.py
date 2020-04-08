# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 10:38:34 2019

@author: morei
"""

le = int(input())
re = int(input())
pe = int(input())
te = int(input())

valid = True

if ((le < 0 or le > 100) or (re<0 or re>100) or (pe<0 or pe>100) or (te<0 or te>100)):
    valid = False
    print("Input error")

if((pe < 40 or te < 40) and valid):
    #valid = False
    print ("RFC")
    
if valid:
    result = (0.1 * le + 0.1 * re + 0.5 * pe + 0.3 * te)*0.2
#    if(result - int(result) >= 0.5):
#        result = int(result) + 1
    print((result))