#!/usr/bin/python3
def best_score(a_dictionary):
    best = (None, -float("inf"))
    if a_dictionary:
        for x, y in a_dictionary.items():
            if y > best[1]:
                best = (x, y)
    if best[1] == -float("inf"):
        return None
    return(best[0])
