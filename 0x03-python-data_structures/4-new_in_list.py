#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    x = 0
    if(idx < 0 or (len(my_list) - 1 < idx)):
        return (None)
    while(x < len(my_list)):
        print("{}".format(my_list[x]))
        x = x + 1