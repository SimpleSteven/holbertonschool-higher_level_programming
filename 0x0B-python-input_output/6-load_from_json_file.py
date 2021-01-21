#!/usr/bin/python3
'''Write a function that creates an Object from a “JSON file”'''
import json


def load_from_json_file(filename):
    '''Open a file, and transform its json strings
    to python structures objects'''
    with open(filename) as file:
        return json.load(file)
