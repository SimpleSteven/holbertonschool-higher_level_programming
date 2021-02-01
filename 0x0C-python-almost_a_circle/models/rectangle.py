#!/usr/bin/python3
''' A new class Rectangle, that
    inherits from Base '''
from base import Base


class Rectangle(Base):
    ''' The Rectangle Class '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Constructor of the Rectangle class
            Args:
                width: the width of the rectangle
                height: the height of the rectangle
                y: the y variable
                x: the x variable
                id: the id of the instance
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        ''' **** The getter of the private ****
            **** instance attribute width **** '''
        return self.__width

    @width.setter
    def width(self, width):
        ''' **** The setter of the private ****
            **** instance attribute width **** '''
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 1:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        ''' **** The getter of the private ****
            **** instance attribute height **** '''
        return self.__height

    @height.setter
    def height(self, height):
        ''' **** The setter of the private ****
            **** instance attribute height **** '''
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 1:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        ''' **** The getter of the private ****
            **** instance attribute x **** '''
        return self.__x

    @x.setter
    def x(self, x):
        ''' **** The setter of the private ****
            **** instance attribute x **** '''
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        ''' **** The getter of the private ****
            **** instance attribute y **** '''
        return self.__y

    @y.setter
    def y(self, y):
        ''' **** The setter of the private ****
            **** instance attribute y **** '''
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
