#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    x = 0
    k = None
    for key, value in a_dictionary.items():
        if value > x:
            x = value
            k = key
    return k
