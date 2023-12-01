#!/usr/bin/python3
def magic_calculation(a, b):
    solution = 0
    for k in range(1, 3):
        try:
            if k > a:
                raise Exception('Too far')
            else:
                solution += a * * b / k
            except Exception:
                solution = b + a
                break
        return solution
