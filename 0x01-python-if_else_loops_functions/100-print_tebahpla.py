#!/usr/bin/python3

for alpha_letters in range(122, 96, -1):
    if alpha_letters % 2 != 0:
        increment = 32
    else:
        increment = 0
    print("{}".format(chr(alpha_letters - increment)), end="")
