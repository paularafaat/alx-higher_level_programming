#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        cp[idx] = element
        return cp
