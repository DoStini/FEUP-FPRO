# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 12:19:47 2019

@author: morei
"""

def mastermind(g1, g2, g3, c1, c2, c3):
    points = 0
    check_1, check_2, check_3 = False, False, False
    if g1 == c1:
        points += 3
        check_1 = True
    else:
        if g1 == c2:
            points += 1
            check_2 = True
        elif g1 == c3:
            points += 1
            check_3 = True
    if g2 == c2:
        if check_2:
            points -= 1
        points += 3
        check_2 = True
    else:
        if g2 == c3:
            points += 1
            check_3 = True
        elif (g2 == c1 and not check_1):
            check_1 = True
            points += 1
    if g3 == c3:
        if check_3:
            points -= 1
        points += 3
    else: 
        if (g3 == c2 and not check_2) or (g3 == c1 and not check_1):
            points += 1
    return(points)
print(mastermind("b", "b", "b", "b", "w", "b"))   