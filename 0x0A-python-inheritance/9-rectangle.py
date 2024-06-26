#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry"""
    def area(self):
        """raises  an Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """String representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
