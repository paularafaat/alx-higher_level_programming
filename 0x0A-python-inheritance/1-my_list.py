#!/usr/bin/python3
"""My list class"""


class Mylist(list):
    """My list class"""
    def print_sorted(self):
        """printing sorted list"""
        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
