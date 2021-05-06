#!/usr/bin/python3


def best_score(a_dictionary):
    val = 0

    if a_dictionary:
        val = max(a_dictionary, key=a_dictionary.get)
        return val
