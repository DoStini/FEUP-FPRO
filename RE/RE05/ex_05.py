# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:14:44 2019

@author: morei
"""

def sort_grades(records):
    records = sorted(records, key=lambda record: record[1])
    records = sorted(records, key=lambda record: record[0])
    records = tuple(sorted(records, key=lambda record: sum(record[2])/len(record[2]), reverse=True))
    return records
