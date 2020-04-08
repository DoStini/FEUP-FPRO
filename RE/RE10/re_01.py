# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:17:59 2019

@author: morei
"""

square_odds = lambda values: ",".join([str(int(x) ** 2) for x in values.split(",") if int(x) % 2 == 1])