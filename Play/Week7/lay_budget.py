# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 13:25:48 2019

@author: morei
"""

def budgeting(budget, products, wishlist):
    total = 0
    for x in list(wishlist.items()):
        total += x[1] * products[x[0]]
    
    item_price = sorted(products.items(), key=lambda x: x[1])
    
    x = 0
    while total > budget:
        item, price = item_price[x][0], item_price[x][1]
        if item in wishlist and wishlist[item] != 0:
            wishlist[item] -= 1
            if wishlist[item] == 0: del wishlist[item]
            total -= price
        else:
            x += 1    
    return wishlist