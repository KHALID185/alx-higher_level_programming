#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence > 0):
        f_l = sentence[0]
    else:
        f_l = None
    lgt = len(sentence)
    return (lgt, f_l)
