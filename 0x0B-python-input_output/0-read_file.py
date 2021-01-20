#!/usr/bin/python3
'''Create a function that reads and print from a given file'''


def read_file(filename=""):
    '''With open, and readlines, print the text of a file'''
    with open(filename) as file:
        print(*file.readlines())
