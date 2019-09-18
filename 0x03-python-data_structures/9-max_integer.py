#!/usr/bin/python3
def max_integer(my_list=[]):
    laragest = 0
    for x in my_list:
        if(x > laragest):
            laragest = x
    return(laragest)
