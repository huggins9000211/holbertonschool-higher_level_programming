#!/usr/bin/python3
def no_c(my_string):
    translation_table = dict.fromkeys(map(ord, 'cC'), None)
    my_string = my_string.translate(translation_table)
    return(my_string)
