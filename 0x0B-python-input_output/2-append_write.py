#!/usr/bin/python3
'''Write a function that appends a string at the end of a
text file (UTF8) and returns the number of characters added'''


def append_write(filename="", text=""):
    '''With open, in mode "a" and with write,
    add a text to a file at the end of the file'''
    with open(filename, mode='a') as file:
        len_of_text = file.write(text)
    return len_of_text
