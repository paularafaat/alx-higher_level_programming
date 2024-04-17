#!/usr/bin/python3
"""JOSN represntation"""
import json


def load_from_json_file(filename):
    """Writting a function that creates an Object from a “JSON file”"""
    with open(filename, "r", encoding="utf-8") as file:
        obj = json.load(file)
    return obj
