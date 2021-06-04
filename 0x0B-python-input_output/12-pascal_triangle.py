#!/usr/bin/python3
'''Pascal Triangle'''


def pascal_triangle(n):
    '''
    This function prints a pascal triangle
    n -- Height of the triangle
    '''

    triangle = []
    row = []
    prev_row = []

    if n <= 0:
        return triangle

    for i in range(0, n + 1):

        row = [j > 0 and j < i -
               1 and i > 2 and prev_row[j-1] +
               prev_row[j] or 1 for j in range(0, i)]

        prev_row = row
        triangle += [row]

    return triangle[1:]
