#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        ls_num = (-number % 10)
    elif number >= 0:
        ls_num = number % 10
    print("{:d}".format(ls_num), end="")
    return ls_num
