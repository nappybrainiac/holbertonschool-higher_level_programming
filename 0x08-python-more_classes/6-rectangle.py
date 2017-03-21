#!/usr/bin/python3
'''
Rectangle - that defines an
instance of a rectangle using width and height.
'''


class Rectangle:
    '''This class defines a rectangle instance.'''

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''initialization'''
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        '''width getter'''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''width setter'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''height getter'''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''making sure the height is a positive integer'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''returns the rectangle's area'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''returns the rectangle's perimeter'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        '''to print #/'s that represent the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = ""
        for i in range(self.__height):
            rect += ("#" * self.__width) + "\n"
        return (rect.rstrip())

    def __repr__(self):
        '''to stringify #/'s that represent the rectangle'''
        return ("Rectangle(%s, %s)" % (str(self.__width), str(self.__height)))

    def __del__(self):
        '''to delete the instance'''
        type(self).number_of_instances -= 1
        print ("Bye rectangle...")
