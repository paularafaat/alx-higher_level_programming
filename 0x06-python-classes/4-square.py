#!/usr/bin/python3
"""square module"""


class Square:
    """Size validation"""
    def __init__(self, size=0):
        """constructor"""
        self.size = size

    @property
    def size(self):
        """getter func"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter func"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """square area function"""
    def area(self):
        return self.__size ** 2
