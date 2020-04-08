# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 13:01:52 2019

@author: morei
"""

s1 = int(input())
s2 = int(input())
s3 = int(input())

result = ""

if (s1 + s2 <= s3 or s1 + s3 <= s2 or s3 + s2 <= s1):
    result = "Not a traingle"
elif(s1 == s2 and s2 == s3):
    result = "Equilateral"
elif(s1 == s2 or s1 == s3 or s2 == s3):
    result = "Isosceles"
else:
    result = "Scalene"
print(result)