#!/usr/bin/python3


if __name__ == "__main__":
    import sys

    if (len(sys.argv) - 1) == 0:
        print('0 arguments.')
    else:
        if (len(sys.argv) - 1) == 1:
            print('{:d} argument:'.format(len(sys.argv) - 1))
        else:
            print('{:d} arguments:'.format(len(sys.argv) - 1))

        for x in range(len(sys.argv)):
            if x != 0:
                print('{:d}: {}'.format(x, str(sys.argv[x])))
