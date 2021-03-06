#!/usr/bin/python3
"""
This file contains a class, Rectangle, that defines an
instance of a rectangle using width and height.
"""


class Rectangle:
    """
    This class defines a rectangle instance.
    """

    def __init__(self, width=0, height=0):
        '''initialization'''
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """making sure the width is a positive integer"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """making sure the height is a positive integer"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        # this is a comment
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            rect += ("#" * self.__width) + "\n"
        return rect.rstrip()

    def __repr__(self):
        return ("Rectangle(%s, %s)" % (str(self.__width), str(self.__height)))
