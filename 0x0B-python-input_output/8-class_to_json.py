#!/usr/bin/python3
"""class to json module"""


def class_to_json(obj):
    """Returns a dictionary representation of an object suitable for JSON serialization"""
    return obj.__dict__
