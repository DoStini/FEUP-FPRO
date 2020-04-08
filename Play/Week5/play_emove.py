# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 23:41:22 2019

@author: morei
"""

def remove_leading(ip):
    ip = ip.split(".")
    for x in range(len(ip)):
        byte_ = list(ip[x])
        while True:
            print(byte_)
            if len(byte_) != 0 and byte_[0] == "0":
                byte_.remove("0")
            else:
                ip[x] = "".join(byte_)
                break
        if len(byte_) == 0:
            byte_.append("0")    
        ip[x] = "".join(byte_)
    return ".".join(ip)