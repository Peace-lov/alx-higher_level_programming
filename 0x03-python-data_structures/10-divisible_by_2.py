#!/usr/bin/python3
def divisible_by_2(my_list = []):
    mylist = my_list[:]
    for count, a in enumerate(my_list):
        if a % 2 == 0:
            mylist[count] = True
        else:
            mylist[count] = False
    return(mylist)
