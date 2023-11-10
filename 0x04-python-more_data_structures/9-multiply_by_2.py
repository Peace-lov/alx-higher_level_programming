#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nw_dict = {}
    for a in a_dictionary:
        nw_dict[a] = a_dictionary[a] * 2
        return nw_dict
