#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
tempnumber = abs(number)
last = tempnumber % 10

if last > 5:
    if number < 0:
        last = -last

    print('Last digit of {:d} is {:d} and is greater than 5'.format(
        number, last))

elif last == 0:
    if number < 0:
        last = -last

    print('Last digit of {:d} is {:d} and is 0'.format(
        number, last))

elif last < 6 and last is not 0:
    if number < 0:
        last = -last

    print('Last digit of {:d} is {:d} and is less than 6 and not 0'.format(
        number, last))
