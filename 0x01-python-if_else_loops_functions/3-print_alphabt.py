#!/usr/bin/python3

for letter_code in range(ord('a'), ord('z')+1):
    if letter_code != 101 and letter_code != 113:
        print("{}".format(chr(letter_code)), end="")
