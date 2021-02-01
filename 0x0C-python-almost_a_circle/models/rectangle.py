#!/usr/bin/python3
''' **** A new class Rectangle, that ****
    **** inherits from id **** '''
from base import Base


class Rectangle(Base):
    ''' **** The Rectangle Class        ****
        **** Attributes:                ****
        **** width, height, y, x and id **** '''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    # width setter
    def set_width(self, width):
        self.__width = width

    # width getter
    def set_width(self):
        return self.__width

    # height setter
    def set_height(self, height):
        self.__height = height

    # height getter
    def set_height(self):
        return self.__height

    # x setter
    def set_x(self, x):
        self.__x = x

    # x getter
    def set_x(self):
        return self.__x

    # y setter
    def set_y(self, y):
        self.__y = y

    # y getter
    def set_y(self):
        return self.__y
