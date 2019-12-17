#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newList = []
    for x in my_list:
        if(x % 2) == 0:
            newList.append(True)
        else:
            newList.append(False)
    return(newList)
