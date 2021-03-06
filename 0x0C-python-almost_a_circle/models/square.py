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
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

    def to_dictionary(self):
        ''' A function that retrieve
            some attributes in a dictionary '''
        attr = ['id', 'x', 'size', 'y']
        return {key: getattr(self, key) for key in attr}

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.height)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
