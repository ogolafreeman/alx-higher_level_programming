#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    numb = 0
    deno = 0

    for tups in my_list:
        numb += tups[0] * tups[1]
        deno += tups[1]

    return (numb / deno)
