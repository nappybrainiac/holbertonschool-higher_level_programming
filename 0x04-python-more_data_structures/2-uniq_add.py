#!/usr/bin/python3
def uniq_add(my_list=[]):
    #for an empty list
    if my_list is None:
        return(None)

    #to create a new list of unique characters
    new_list = set(my_list)
    return sum(new_list)
