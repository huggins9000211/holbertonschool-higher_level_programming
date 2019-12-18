#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    laragest = -float('inf')
    for x in my_list:
        if(x > laragest):
            laragest = x
    return(laragest)
