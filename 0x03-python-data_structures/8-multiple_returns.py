#!/usr/bin/python3
def multiple_returns(sentence):
    lgt = len(sentence)
    if (lgt > 0):
        f_l = sentence[0]
    else:
        return None
    return (lgt, f_l)
