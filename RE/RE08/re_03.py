# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:22:32 2019

@author: morei
"""

def file_finder(dirs, file_name):
    new = ""
    for idx, x in enumerate(dirs):
        if type(x) == list:
            val = file_finder(x, file_name)
            if val != None:
                new = dirs[0] + "/" + val
                return new
        elif idx != 0:
            if x == file_name:
                return dirs[0] + "/" + file_name
    return None