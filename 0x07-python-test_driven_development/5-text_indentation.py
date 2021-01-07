#!/usr/bin/python3
'''
    A function that print a large string with
    2 new lines after these characters: ., ? and :
    Functions:
        text_indentation(text)
'''


def text_indentation(text):
    '''
    Args:
        text: a large string to print
    Raises:
        TypeError:
        If text isn't a string
    '''

    if type(text) != str:
        raise TypeError("text must be a string")
    if 0 == len(text) or 1 == len(text):
        print(text, end="")
        return
    for character in [".", "?", ":"]:
        text = text.replace(character, character + "\n")
    str_list = text.split("\n")
    text = ""
    for string in str_list:
        text += string.strip()
    for character in [".", "?", ":"]:
        text = text.replace(character, character + "\n\n")
    print(text, end="")
