#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """rectnagle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        self.validate_attribute("width", value)
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        self.validate_attribute("height", value)
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        self.validate_attribute("x", value)
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        self.validate_attribute("y", value)
        self.__y = value

    def validate_attribute(self, name, value):
        """validator for attributes"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if name in ["width", "height"] and value <= 0:
            raise ValueError(f"{name} must be > 0")

        if name in ["x", "y"] and value < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """calculate the area of rectangle"""
        return self.width * self.height

    def display(self):
        """display the rectangle with # characters"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """return string representation of Rectangle"""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}")

    def update(self, *args):
        """update rectangle attributes with positional arguments"""

        self.id = args[0]
        self.width = args[1]
        self.height = args[2]
        self.x = args[3]
        self.y = args[4]
