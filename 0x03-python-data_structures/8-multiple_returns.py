#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence is "":
        return 0, None

    string_len = len(sentence)
    first_c = sentence[0]
    return string_len, first_c
