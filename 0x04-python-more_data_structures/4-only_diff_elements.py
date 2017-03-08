#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 is None:
        return None
    elif set_2 is None:
        return None
    else:
        return [i for i in set_1 if i not in set_2]
