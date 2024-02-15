#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    try:
        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end='')
                i += 1
    except (ValueError, TypeError, IndexError):
        None
    print()
    return i
