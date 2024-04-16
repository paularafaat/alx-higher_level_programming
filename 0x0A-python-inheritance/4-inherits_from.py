#!/usr/bin/python3
"""module for checking types"""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a subclass of a_class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
