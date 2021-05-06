#!/usr/bin/python3


def roman_to_int(roman_string):
    if isinstance(roman_string, str) or roman_string is not None:
        romans = {
            'I': 1, 'V': 5,
            'X': 10, 'L': 50,
            'C': 100, 'D': 500,
            'M': 1000
        }

        roman_backward = list(reversed(list(roman_string)))
        val = 0

        right = romans[roman_backward[0]]

        for n in roman_backward:
            left = romans[n]

            if left < right:
                val -= left
            else:
                val += left

            right = left

        return val
    else:
        return 0
