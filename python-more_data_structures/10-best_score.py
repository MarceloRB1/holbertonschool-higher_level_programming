#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    i = list(a_dictionary.values())
    x = list(a_dictionary.keys())

    return (x[i.index(max(i))])
