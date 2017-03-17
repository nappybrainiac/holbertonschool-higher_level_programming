#!/usr/bin/python3
"""
This file contains one class Square
"""
class Square:
    """
    This class defines a square that allows for intantiation
    with a particular size.
    """

    def __init__(self, size=0):
        """ Initialization function"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
