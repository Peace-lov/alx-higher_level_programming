#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    arg_c = len(argv)
    if arg_c != 4:
        print('Usage: {} <a> <operator> <b>'.format(argv[0]))
        exit(1)
    ops = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    if argv[2] in ops:
        nums1 = int(argv[1])
        nums2 = int(argv[3])
        op = ops[argv[2]]
        res = op(nums1, nums2)
        print('{:d} {:s} {:d} = {:d}'.format(nums1,
            argv[2], nums2, res))
    else:
        print('Unknown operator. Available operators: +, -, *, and /')
        exit(1)
    exit(0)
