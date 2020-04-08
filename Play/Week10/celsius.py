# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:47:34 2019

@author: morei
"""

to_celsius = lambda t: [round((x-32)/1.8, 1) for x in t]