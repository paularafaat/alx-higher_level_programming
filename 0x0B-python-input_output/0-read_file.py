#!/usr/bin/python3
"""read file module"""


def read_file(filename=""):
    """reading a file"""
    with open(filename, encoding="utf-8") as f:
        content = f.read()
        print(content)