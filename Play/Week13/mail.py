# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 22:27:47 2020

@author: morei
"""

def mail_merge(names, mail_template):
    
    with open(names, "r") as file:
        names = file.read().split("\n")[:-1]
    with open(mail_templates, "r") as file:
        mail = file.read()
    
    out = []
    
    for x in names:
        out.append(mail.replace("<name>", x))
    
    return out