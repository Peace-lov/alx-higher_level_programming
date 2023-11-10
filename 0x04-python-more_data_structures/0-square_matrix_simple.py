#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nw_matx = [r[:] for r in matrix]
    for index, r in enumerate(nw_matx):
        for index2, colu in enumerate(nw_matx):
            nw_matx[index][index2] = r[index2] ** 2
    return nw_matx
