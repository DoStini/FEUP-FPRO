# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 21:40:47 2019

@author: morei
"""

def dogs(h_age):
    if h_age <= 2:
        return(h_age * 10.5)
    else:
        return(2*10.5 + (h_age - 2) * 4)