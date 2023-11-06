#!/usr/bin/python3
def no_c(my_string):
    char_to_move = ['c', 'C']
    for a in my_string:
        if a == char_to_move:
            continue
        else:
            return my_string
