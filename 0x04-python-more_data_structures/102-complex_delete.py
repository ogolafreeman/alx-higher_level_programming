#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for value_d in list_keys:
        if value == a_dictionary.get(value_d):
            del a_dictionary[value_dic]

    return (a_dictionary)
