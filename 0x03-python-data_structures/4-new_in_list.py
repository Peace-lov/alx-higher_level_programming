#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    replace_list = my_list[:]
    if 0 <= idx < len(my_list):
        replace_list[idx] = element
        return (replace_list)
    return (my_list)

