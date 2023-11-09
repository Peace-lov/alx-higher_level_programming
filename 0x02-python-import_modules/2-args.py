#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg = sys.argv
    length = len(sys.argv) - 1
    if length == 0:
        print("{} argument.".format(length))
    if length > 1:
        print("{} arguments:".format(lenght))
        for a in range(1, lenght + 1):
            print("{} : {}".format(length, arg[a]))
    else:
        print("{} arguments:".format(length))
        print("{} : {}".format(length, arg[1]))
