# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 11:13:08 2019

@author: morei
"""

def permutations(atuple):
    pass
    
    
    
    
def permuta(alist, step=0):
    alist = list(alist)
    lista = []
    for x in range(len(alist)):
        alist_copy = alist.copy()
        alist_copy[x] = alist[0]
        alist_copy[0] = alist[x]
        if alist_copy not in lista:     
            lista.append(alist_copy)
        new_list = [alist_copy[0]]
        lists = permuta(alist_copy[1:], 1)
        for val in lists:
            if val is not None:
                lista.append(new_list + val)
    output = []
    for x in lista:
        if x not in output:
            output.append(x)
    if step == 0:
        output = map(lambda x: tuple(x), output)
        return set(output)
    else:
        return output
    
    
    
#    def recursive(atuple, step=0):
#        atuple = list(atuple)
#        lista = []
#        if len(atuple) == 1:
#            if step == 1: 
#                return atuple 
#            else: 
#                return atuple[0]
#        elif len(atuple) == 2:
#            if step == 1:
#                return [atuple[1], atuple[0]] 
#            else: 
#                return ((atuple[0], atuple[1]), (atuple[1], atuple[0]))
#        else:
#            for x in range(len(atuple)):
#                new = atuple.copy()
#                temp = new[0]
#                new[0] = new[x]
#                new[x] = temp
#                lista.append(tuple(new))
#                val1 = [new[0]]
#                val2 = recursive(new[1:])
#                if val2 is not None:
#                    for sublist in val2:
#                        if sublist is not None and val1 is not None:
#                            lista.append(tuple(val1.extend(list(sublist))))
#            
#        return lista
#    return set(recursive(atuple))