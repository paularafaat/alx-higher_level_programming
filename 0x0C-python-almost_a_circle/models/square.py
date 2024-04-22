#!/usr/bin/python3
"""square module"""
from models import rectangle


class Square(rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
