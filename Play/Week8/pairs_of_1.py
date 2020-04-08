# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 17:02:29 2019

@author: morei
"""

#def no_consecutives(k):
#    iterations = 2 ** k
#    return recursive(0, iterations)
#
#def recursive(curr, max_iter):
#    dic = {True:1, False:0}
#    if curr != max_iter:
#        temp = str(bin(curr)[2:])
#        if "11" in temp:
#            val = True
#        else:
#            val = False
#        next_num = recursive(curr + 1, max_iter)
#        return dic[val] + next_num
#    else:
#        return 0

def no_consecutives1(k):
    return len([x for x in range(2**k) if "11" not in str(bin(x))])

#def check_num(num): 
#    if num < 10:
#        return True
#    else:
#        if num%10 == (num//10) % 10 and num%10 == 1:
#            return False
#        val = check_num(num//10)
#        if val:
#            return True
#        else:
#            return False


#def countStrings(n): 
#  
#    a=[0 for i in range(n)] 
#    b=[0 for i in range(n)] 
#    a[0] = b[0] = 1
#    for i in range(1,n): 
#        a[i] = a[i-1] + b[i-1] 
#        b[i] = a[i-1] 
#      
#    return a[n-1] + b[n-1] 