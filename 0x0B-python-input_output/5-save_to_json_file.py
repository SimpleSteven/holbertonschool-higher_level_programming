#!/usr/bin/python3
'''Write a function that writes an Object to a
text file, using a JSON representation'''
import json


def save_to_json_file(my_obj, filename):
    ''' Run open with write, and write into the file,
    a json serialization of an object'''
    with open(filename, mode='w') as file:
        json.dump(my_obj, file)
