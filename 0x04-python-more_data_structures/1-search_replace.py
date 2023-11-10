#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    nwlist = my_list[:]
    for index, a in enumerate(nwlist):
        if a == search:
            nwlist[index] = replace
    return nwlist
