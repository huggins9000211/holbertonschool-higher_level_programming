def replace_in_list(my_list, idx, element):
    if(idx < 0 or (len(my_list) - 1 < idx)):
        return (None)
    my_list[idx] = element