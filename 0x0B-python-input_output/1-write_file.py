#!/usr/bin/python3
"""write file module"""


def write_file(filename="", text=""):
    """writing in file"""
    with open(filename, "w", encoding='utf-8') as file:
        num_written = file.write(text)
    return num_written
