#!/usr/bin/python3
"""square module"""


class Square:
    """Coordinates of a square"""
    def __init__(self, size=0, position=(0, 0)):
        """constructor"""
        self.size = size
        self.position = position

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

    @property
    def position(self, value):
        """getter func"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter func"""
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(num, int) for num in value) \
                or any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    """square area function"""
    def area(self):
        return self.__size ** 2

    def my_print(self):
        """printing a square with # char"""
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
