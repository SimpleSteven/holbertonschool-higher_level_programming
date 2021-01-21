#!/usr/bin/python3
''' Write a function that returns the JSON
representation of an object (string)'''
import json


def to_json_string(my_obj):
    ''' Convert the object passed, to a json
    representation and return it'''
    new_json = json.dumps(my_obj)
    return new_json
