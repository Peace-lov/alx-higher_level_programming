#!/usr/bin/python3
def add_arg(argv):
    size = len(argv) - 1
    if size == 0:
        print("{:d}".format(size))
        return
    else:
        a = 1
        add = 0
        while a <= size:
            add += int(argv[a])
            a += 1
        print("{:d}".format(add))

if __name__ == "___main__":
    import sys
    add_arg(sys.argv)
