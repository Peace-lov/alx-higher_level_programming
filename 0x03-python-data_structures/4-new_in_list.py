#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    replace_list = my_list[0:]
    if idx < 0:
        return my_list
    elif idx >=len(my_list):
        return my_list
    else:
        replace_list[idx] = element
        return replace_list
    return my_list
