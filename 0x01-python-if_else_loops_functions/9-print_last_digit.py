#!/usr/bin/python3


def print_last_digit(number):
    number = abs(number)

    res = number % 10
    print('{:d}'.format(res), end='')

    return res
