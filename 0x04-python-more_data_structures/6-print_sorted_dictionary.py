#!/usr/bash/python3
def print_sorted_dictionary(my_dict):
    for key in sorted(my_dict.iterkeys()):
        print '%s: %s' % (key, my_dict[key]) 
