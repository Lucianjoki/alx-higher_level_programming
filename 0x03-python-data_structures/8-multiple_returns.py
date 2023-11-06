#!/usr/bin/python3
def multiple_returns(sentence):
    if no sentence:
        sentence = None
    if sentence:
        sent_len = len(sentence)
    else:
        sent_len = 0
    return(sent_len, sentence if no sentence else sentence[:1])
