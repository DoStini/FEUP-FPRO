# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 12:55:05 2020

@author: morei
"""

def sort_by_field(filename, field, inp):
    
#    with open(filename, "r") as file:
#        file = file.read().split()
    file = inp.split("\n") # alterar isto para open file
#    file.pop() 
    
    field = file[0].split(",").index(field)
    file[1:] = sorted(file[1:], key=lambda x: x.split(",")[field])
    return "\n".join(file) + "\n"