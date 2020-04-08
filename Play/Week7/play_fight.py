# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 10:07:38 2019

@author: morei
"""

def fight(heroes, villain):
    for hero in heroes:
        if hero["category"] == villain["category"]:
            if hero["health"] >= villain["health"]:
                return f'{hero["name"]} defeated the villain and now has a score of {hero["score"] + 1}'
            else:
                villain["health"] -= hero["health"]/2
    return f'{villain ["name"]} 1prevailed with {round(villain["health"], 1)}HP left'