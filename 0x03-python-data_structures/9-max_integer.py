#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_value = my_list[0]  # Initialize max with the first element of the list
    for num in my_list:
        if num > max_value:
            max_value = num
    return max_value
