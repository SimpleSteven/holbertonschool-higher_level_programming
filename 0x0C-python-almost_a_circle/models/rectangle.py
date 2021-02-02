#!/usr/bin/python3
''' A new class Rectangle, that
    inherits from Base '''
from models.base import Base


class Rectangle(Base):
    ''' The Rectangle Class
        Args:
            width: the width of the rectangle
            height: the height of the rectangle
            y: the y variable
            x: the x variable
            id: the id of the instance
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def display(self):
        ''' Print in stdout the rectangle
            with the "#" character '''
        print('\n' * self.y + (' ' * self.x + "#" * self.width + '\n') *
              self.height, end='')

    def area(self):
        '''The area of the rectangle
            is width by height'''
        return self.width * self.height

    def update(self, *args, **kwargs):
        ''' Function that update the value of
            the instance attributes '''
        if len(args) == 0:
            keys = kwargs.keys()
            for key in keys:
                try:
                    getattr(self, key)
                except AttributeError:
                    continue
                setattr(self, key, kwargs.get(key))
        else:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass

    def to_dictionary(self):
        ''' A function that retrieve
            some attributes in a dictionary '''
        attr = ['x', 'y', 'id', 'height', 'width']
        return {key: getattr(self, key) for key in attr}

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 1:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 1:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
