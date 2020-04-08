# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 19:33:06 2019

@author: morei
"""

def knapsack(money, products, wishlist):
    def recursive_knapsack(money, wishlist, basket):
        baskets = []
        
        if len(wishlist) == 0:
            return (money, basket)
        for item in wishlist:
            item_price = products[item]
            
            if money - item_price < 0:
                return (money, basket)
            else:
                new_basket = basket.copy()
                new_basket[item] = new_basket.get(item, 0) + 1
                new_money = money - item_price
                new_wishlist = wishlist.copy()
                new_wishlist[item] -= 1
                if new_wishlist[item] <= 0:
                    del new_wishlist[item]
                    
                baskets.append(recursive_knapsack(new_money, new_wishlist, new_basket))
                
        return list(sorted(baskets))[0]
    
    return recursive_knapsack(money, wishlist, {})[1]