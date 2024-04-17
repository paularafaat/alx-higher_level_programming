#!/usr/bin/python3
"""JOSN represntation"""
import json


def from_json_string(my_str):
    """Returns a Python data"""
    return json.loads(my_str)
