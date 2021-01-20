#!/usr/bin/python3
'''Write a function that writes a string to a text file (UTF8) and returns the number of characters written'''

def write_file(filename="", text=""):
    '''With open, in mode "w" and with write, add a text to a file'''
    with open(filename, mode='w') as file:
        len_of_text = file.write(text)
    return len_of_text
