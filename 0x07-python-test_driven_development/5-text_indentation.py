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
    for character in [". ", "? ", ": "]:
        text = text.replace(character, character[0] + "\n\n")
    print(text)


text_indentation("He said: What.")