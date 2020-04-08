# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 15:46:58 2019

@author: morei
"""

A = input()
B = input()

if A=="rock":
    if B == "rock":
        print("That's a draw")
    elif B == "paper":
        print("The winner is B")
    else:
        print("The winner is A")
elif A=="paper":
    if B == "rock":
        print("The winner is A")
    elif B == "paper":
        print("That's a draw")
    else:
        print("The winner is B")
else:
    if B == "rock":
        print("The winner is B")
    elif B == "paper":
        print("The winner is A")
    else:
        print("That's a draw")

