#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg = sys.argv
    length = len(arg) - 1
    if length > 1:
        print("{} arguments:".format(length))
        for a in range(1, length + 1):
            print("{}: {}".format(a, arg[a]))
    elif length == 0:
        print("{} arguments.".format(length))
    else:
        print("{} arguments:".format(length))
        print("{}: {}".format(length, arg[1]))
