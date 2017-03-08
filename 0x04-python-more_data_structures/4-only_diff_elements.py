#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
        unity = set(set_1).union(set(set_2))
        intersect = set(set_1).intersection(set(set_2))
        return list(unity - intersect)
