#!/usr/bin/python3
def multiple_returns(sentence):
    lgt = len(sentence)
    if not lgt > 0:
        return (0, None)
    return (lgt, sentence[0])
