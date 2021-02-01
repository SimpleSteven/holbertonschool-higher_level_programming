#!/usr/bin/python3
''' A new class Square, that
    inherits from Rectangle '''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' The Square Class
        Args:
            size: the width and height of the Square
            y: the y variable
            x: the x variable
            id: the id of the instance
    '''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.size = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.height)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
        self.__size = size
