#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        a = max(sorted(a_dictionary.values()))
        for j, n in a_dictionary.items():
            if a == n:
                return(j)
    else:
        return (None)
