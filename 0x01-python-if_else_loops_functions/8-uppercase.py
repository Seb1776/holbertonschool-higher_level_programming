#!/usr/bin/python3


def uppercase(str):
    for chars in range(0, len(str)):
        if (ord(str[chars]) >= 97 and ord(str[chars]) <= 122):
            x = 32
        else:
            x = 0

        y = ord(str[chars]) - x
        print('{}'.format(chr(y)), end='')

    print('')
