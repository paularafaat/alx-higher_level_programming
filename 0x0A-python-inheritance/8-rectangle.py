#!/usr/bin/python3
"""Rectangle class"""


BaseGeometry = __import___("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
