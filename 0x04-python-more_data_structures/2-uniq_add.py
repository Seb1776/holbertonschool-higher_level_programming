#!/usr/bin/python3


def uniq_add(my_list=[]):
    res = []
    ress = 0

    [res.append(x) for x in my_list if x not in res]

    for y in range (len(res)): 
        ress += res[y]

    return ress
