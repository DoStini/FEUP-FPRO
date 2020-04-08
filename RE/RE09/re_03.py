# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 12:28:25 2019

@author: morei
"""

#def invoice_totals(orders, min):
#    orders = 
#    return orders

invoice_totals = lambda orders, min: list(map(lambda x: (x[0], x[2]*x[3]) if x[2]*x[3] > min else (x[0], x[2]*x[3] +10), orders))