#!/usr/bin/python3
"""write file module"""


def append_write(filename="", text=""):
    """Appending a string to a file"""
    with open(filename, 'a', encoding='utf-8') as file:
        num_added = file.write(text)
    return num_added
