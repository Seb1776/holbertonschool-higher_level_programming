#!/usr/bin/python3


if __name__ == "__main__":
    from calculator1 import add
    a = 10
    b = 5
    print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))

    from calculator1 import sub
    a = 10
    b = 5
    print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))

    from calculator1 import mul
    a = 10
    b = 5
    print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))

    from calculator1 import div
    a = 10
    b = 5
    print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
