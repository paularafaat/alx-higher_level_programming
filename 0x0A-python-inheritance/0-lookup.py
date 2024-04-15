#!/usr/bin/python3
"""returning a list of obj"""


def lookup(obj):
    """return s list of object

    Args:
        obj (str):

    Returns:
        list: list of object
    """
    return dir(obj)
