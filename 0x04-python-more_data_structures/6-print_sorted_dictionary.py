#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_ord = list(a_dictionary.keys())
    list_ord.sort()
    for y in list_ord:
        print("{}: {}".format(y, a_dictionary.get(y)))
