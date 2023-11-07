#!/usr/bin/python3
def no_c(my_string):
    char_to_move = ""
    for a in my_string:
        if a != 'c' and a != 'C':
            char_to_move += a
        return char_to_move
