#!/usr/bin/python3
"""class to json module"""


def class_to_json(obj):
    """Returns a dictionary representation"""
    return obj.__dict__
