#!/usr/bin/python3
"""read file module"""


def read_file(filename=""):
    """reading a file"""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
