'''
Project:            Basic OOP with Python
Dependent files:    3-main.py

The function in this file computes the fibonacci number of
a given number. In this method, recursion has been used.

Gloria Bwandungi, 2016.
'''
import math

'''Class'''
class Circle(object):

    ''' Constructor '''
    def __init__(self, radius):
        self.__radius = radius

    ''' Setters '''
    def set_center(self, center):
        self.__center = center

    def set_color(self, color):
        self.__color = color

    def set_name(self, name):
        self.name = name

    def area(self):
        return (self.__radius ** 2) * math.pi

    ''' Getters '''
    def get_color(self):
        return self.color

    def get_center(self):
        return self.center
