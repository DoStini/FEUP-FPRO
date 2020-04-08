# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 21:20:13 2019

@author: morei
"""
def validate(number):
    return (type(number) == float or type(number) == int) and 0 <= number <= 100