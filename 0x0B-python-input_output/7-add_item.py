#!/usr/bin/python3
'''Write a script that adds all arguments to a
Python list, and then save them to a file'''
import sys
import os.path
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args_from_json = []
if path.exists('add_item.json'):
    with open('add_item.json') as file:
        if not file.read() == '':
            args_from_json = list(load_from_json_file('add_item.json'))
args_to_json = [arg for arg in sys.argv[1:]]
args_from_json.extend(args_to_json)
save_to_json_file(args_from_json, 'add_item.json')
