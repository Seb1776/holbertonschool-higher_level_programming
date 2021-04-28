#!/usr/bin/python3


import sys

if (len(sys.argv) - 1) == 0:
    print('0 arguments.')
else:
    print('{:d} arguments:'.format(len(sys.argv) - 1))
    for x in range(len(sys.argv)):
        if x != 0:
            print('{:d}: {}'.format(x, str(sys.argv[x])))
