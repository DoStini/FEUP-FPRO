from math import ceil

def digits_average(n):
    len_ = 0
    aux_n = n
    while aux_n > 0:
        len_ += 1
        aux_n = aux_n//10 
    aux_n = n
    
    while len_ != 1:
        aux_n = sum_line(len_, aux_n)
        len_ -= 1
    return(aux_n)

def sum_line(len_, aux_n):
    sum = 0
    for x in range(1, len_):
        len_ -= 1
        n1 = aux_n % 10
        aux_n = aux_n //10
        n2 = aux_n % 10
        mean = ceil((n1+n2)/2)
        sum += mean * 10**(x-1)
    return(sum)
    
print(digits_average(1))