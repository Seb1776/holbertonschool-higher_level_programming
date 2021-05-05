#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    i = 0

    if matrix is not None:
        for mx in matrix:
            if i == 3:
                print('')
                i = 0

            for my in mx:
                i += 1

                if i != 3:
                    print('{}'.format(my), end=' ')
                else:
                    print('{}'.format(my), end='')

        print('')
