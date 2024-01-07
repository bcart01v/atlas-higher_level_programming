#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) <= 0:
        return
    first = sentence[0:1]
    count = len(sentence)

    return(count, first)
