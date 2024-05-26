#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]
print(return_evens(range(10)))

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]
print(make_exclamation(["I like computers", "I require coffee", "Live long and prosper"]))