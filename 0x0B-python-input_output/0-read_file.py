#!/usr/bin/python3
"""read file module"""


def read_file(filename=""):
    """reading a file"""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line)
