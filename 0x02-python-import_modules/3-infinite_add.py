#!/usr/bin/python3


if __name__ == "__main__":
    import sys

    y = 0
    if (len(sys.argv) - 1) == 0:
        print('0')
    else:
        for x in range(1, len(sys.argv)):
            y += int(sys.argv[x])

        print(y)
