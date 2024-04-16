#!/usr/bin/python3
"""module for checking types"""


def is_same_class(obj, a_class):
    """checking if the same class

    Args:
        obj (object):
        a_class (class):
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
