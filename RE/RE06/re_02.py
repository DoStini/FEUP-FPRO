# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 12:00:24 2019

@author: morei
"""

def mult(M, N):
    result = []

    if len(M[0]) == len(N):
        for x in range(len(M)):
            result.append([])
            for y in range(len(N[0])):
                result[x].append(0)
        for x in range(len(M)):
            for y in range(len(N[0])):
                for z in range(len(N)):
                    result[x][y] += M[x][z] * N[z][y]
        return result
    else:
        return []