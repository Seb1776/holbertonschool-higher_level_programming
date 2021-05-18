#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    res = 0

    for x in range(list_length):
        try:
            res = my_list_1[x] / my_list_2[x]
        except (TypeError, ValueError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print('out of range')
        finally:
            res_list.append(res)
    
    return res_list
