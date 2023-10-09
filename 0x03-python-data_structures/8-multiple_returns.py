#!/usr/bin/python3
def multiple_returns(sentence):
    L = len(sentence)
    c = sentence[0]
    if L == 0:
        result = L, None
    else:
        result = L, c
    return result
