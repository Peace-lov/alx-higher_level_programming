#!/usr/bin/python3
def multiple_returns(sentence):
    len_of_tuple = len(sentence)
    char_fst = sentence[0] if len_of_tuple > 0 else "None"
    tupl = len_of_tuple, char_fst
    return (tupl)
