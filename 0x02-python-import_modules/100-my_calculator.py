#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    arg_c = len(argv)
    if atg_c != 4:
        print('Usage: {} <a> <operator> <b>'.format
                (argv[0]))
        exit(1)
    ops = {
            '+' : add,
            '-' : sub,
            '*' : mul,
            '/' : div
        }
    if argv[2] in ops:
        numb1 = int(argv[1])
        numb2 = int(argv[3])
        op = ops[argv[2]]
        res = op(numb1, numb2)
        print('{:d} {:s} {:d} = {:d}'.format(numb1,
            argv[2], numb2, res))
    else:
        print('Unknown operator. Available operators: +, -,
        *, and /')
        exit(1)
    exit(0)
