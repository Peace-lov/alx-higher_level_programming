#!/usr/bin/python3
from magic_calculation_102 import add, sub

def magic_calculation(a, b):
    if a < b:
        cal = add(a, b)
        for a in range(4, 6):
            cal = add(cal, a)
        return (cal)
    else:
        return sub(a, b)
