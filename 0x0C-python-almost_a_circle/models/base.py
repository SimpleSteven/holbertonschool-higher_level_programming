#!/usr/bin/python3
''' **** A new class Base, that ****
    **** handles the ids of the   ****
    **** objects               **** '''
import json


class Base:
    ''' **** The Base Class **** '''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' Function that returns the JSON string
            representation of list_dictionaries '''
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)
