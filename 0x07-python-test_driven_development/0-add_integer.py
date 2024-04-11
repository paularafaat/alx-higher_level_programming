#!/usr/bin/python3
"""Module for add_integer method."""


def add_integer(a, b=98):
    """fun to add two nubmers

    Args:
        a (int, float): argument
        b (int, float): argument

    Raises:
        TypeError: if a or b not integer or float

    Returns:
        integer: the addetion of a , b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
