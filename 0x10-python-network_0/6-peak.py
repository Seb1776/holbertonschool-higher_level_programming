#!/usr/bin/python3
"""Function to Find a Peak i na list of numbers"""


def find_peak(list_of_integers):
    """Finds a peak in a list of numbers"""

    if list_of_integers == []:
        return None

    size = len(list_of_integers)

    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    middle = int(size / 2)
    left = list_of_integers[middle - 1]
    right = list_of_integers[middle + 1]
    peak = list_of_integers[middle]

    if peak > left and peak > right:
        return peak
    elif peak < left:
        return find_peak(list_of_integers[:middle])
    else:
        return find_peak(list_of_integers[middle + 1:])
