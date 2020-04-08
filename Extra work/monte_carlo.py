# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:25:25 2019

@author: André Moreira
"""
import random
import math
import statistics
import time

START_TIME = time.time()


def get_results(cicle):
    pi_results = []
    for _x in range(100):
        position = [0, 0]  # index 0: in circle   index 1: outside circle
        for _y in range(cicle):
            x, y = random.uniform(-1, 1), random.uniform(-1, 1)  # Random pos
            dist = math.sqrt(x**2 + y**2)  # Distance to origin
            if (dist < 1):
                position[0] += 1
        pi_results.append(4 * position[0] / cicle)
    print(statistics.stdev(pi_results))
    if (not statistics.stdev(pi_results) < 0.005):
        print(cicle)
        cicle *= 2
        get_results(cicle)
    return(statistics.mean(pi_results))


print(get_results(1000))

print("%s seconds" % (time.time() - START_TIME))
input()
