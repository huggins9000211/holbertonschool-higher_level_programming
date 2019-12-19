#!/usr/bin/python3
def uniq_add(my_list=[]):
    sumT = 0
    list_set = set(my_list)
    new_list = list(list_set)
    for x in new_list:
        sumT += x
    return sumT
