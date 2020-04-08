# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:42:04 2019

@author: morei
"""

import random


num = int(input())
x_init = random.random() * num
x_end = (x_init + num/x_init)/2
converged = (round(x_init, 2) == round(x_end, 2))
iter_ = 0
while True:
    iter_ += 1
    if converged:
        break
    x_init = x_end
    x_end = (x_init + num/x_init)/2
    converged = (round(x_init, 2) == round(x_end, 2))
print(round(x_end, 3))
