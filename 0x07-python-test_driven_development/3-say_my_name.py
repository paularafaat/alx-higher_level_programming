#!/usr/bin/python3
"""Module for say my name"""


def say_my_name(first_name, last_name=""):
    """fun to print name

    Args:
        first_name (str): first name
        last_name (str, none): last name. Defaults to "".
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or \
last_name must be a string")
    print("My name is " + first_name + " " + last_name)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
