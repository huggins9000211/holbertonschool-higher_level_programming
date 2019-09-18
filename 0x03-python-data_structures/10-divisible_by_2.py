#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newList = []
    i = 0
    for x in my_list:
        if(x % 2) == 0:
            newList[i] = True
        else:
            newList[i] = False
    return(newList)