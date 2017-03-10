#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = my_dict.copy()
    for value in new_dict:
        value *= 2
    return new_dict
