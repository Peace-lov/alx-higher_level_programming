#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    ndic = {key: value}
    a_dictionary.update(ndic)
    return a_dictionary
