# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 15:54:23 2019

@author: morei
"""


to_celsius = lambda t: list(map(lambda x: round((x-32)/1.8, 1), t))