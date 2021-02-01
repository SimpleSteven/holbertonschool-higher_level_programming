#!/usr/bin/python3
''' **** A new class Rectangle, that ****
    **** inherits from id **** '''
from base import Base


class Rectangle(Base):
    ''' **** The Rectangle Class        ****
        **** Attributes:                ****
        **** width, height, y, x and id **** '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' **** Constructor of the Rectangle ****'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        self.__y = y
