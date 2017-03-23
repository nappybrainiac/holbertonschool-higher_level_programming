class Rectangle():
    '''class Rectangle - Parameters(width(int), height(int))'''

    number_of_instances = 0  # Count instances created and deleted
    print_symbol = '#'  # Symbol for string representation

    def __init__(self, width=0, height=0):
        ''' Constructor '''
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        ''' Overload __str__ to print rectangle. '''
        if self.__width == 0 or self.__height == 0:
            return ''
        # Build a visual representation of the rectangle.
        b = ((str(self.print_symbol) * self.__width + '\n') * self.__height)
        # Return the rectangle after stripping the trailing newline.
        return (b.strip('\n'))

    def __repr__(self):
        ''' Overload __repr__ to return string. '''
        return("Rectangle(%d, %d)" % (self.__width, self.__height))

    def __del__(self):
        ''' On delete print confirmation. '''
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        ''' Getter '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' Setter '''
        if isinstance(value, int):
            if value < 0:
                raise ValueError('width must be >= 0')
            self.__width = value
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        ''' Getter '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' Setter '''
        if isinstance(value, int):
            if value < 0:
                raise ValueError('height must be >= 0')
            self.__height = value
        else:
            raise TypeError('height must be an integer')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' Compare both rectangles and return the biggest based on area '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        # Compare both rectangles. Return rect_1 if both are of the same area.
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        ''' Class method that returns a rectangle of equal width and height '''
        return (cls(size, size))

    def area(self):
        ''' Returns the rectangle area '''
        return self.__width * self.__height

    def perimeter(self):
        ''' Returns the rectangle perimeter. '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
