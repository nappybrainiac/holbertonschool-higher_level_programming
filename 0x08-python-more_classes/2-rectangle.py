#!/usr/bin/python3
"""
This file contains a class, Rectangle, that defines an
instance of a rectangle using width and height.
"""


class Rectangle:
    """
    This class defines a rectangle instance.
    """

    w_int = "width must be an integer"
    w_pos = "width must be >= 0"
    h_int = "height must be an integer"
    h_pos = "height must be >= 0"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """making sure the width is a positive integer"""
        if type(value) is not int:
            raise TypeError(w_int)
        elif value < 0:
            raise ValueError(w_pos)
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """making sure the height is a positive integer"""
        if type(value) is not int:
            raise TypeError(h_int)
        elif value < 0:
            raise ValueError(h_pos)
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            self.__perimeter = 0
        return (self.__width * 2) + (self.__height * 2)
