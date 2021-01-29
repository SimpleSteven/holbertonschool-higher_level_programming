#!/usr/bin/python3
''' **** A new class Base, that ****
    **** handles the ids of the   ****
    **** objects               **** '''


class Base:
    ''' **** The Base Class **** '''

    __nb_objects = 0

    def __init__(self, id=None):
        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
