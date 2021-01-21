#!/usr/bin/python3
'''Write a function that returns the dictionary description
with simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object'''
import json


def class_to_json(obj):
    '''A function that do something
    I'm sleepy...'''
    public_attr = [name for name in dir(obj) if not name.startswith('_')]
    attr_dict = {}
    for attr in public_attr:
        attr_dict.update({attr: getattr(obj, attr)})
    return attr_dict
