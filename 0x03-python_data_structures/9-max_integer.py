#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) <= 0:
        return None

    current_highest = 0
    j = 0

    for i in my_list:
        if j == 0:
            current_highest = i
        else:
            if i > current_highest:
                current_highest = i

        j += 1

    return current_highest
