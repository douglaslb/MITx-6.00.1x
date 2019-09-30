# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:49:13 2019

@author: doohl
"""

def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict


she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 'yeah', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah', 'you', 'think', "you've", 'lost', 'your', 'love', 'well,', 'i', 'saw', 'her', 'yesterday', "it's", 'you', "she's", 'thinking', 'of', 'and', 'she', 'told', 'me', 'what', 'to', 'sayshe', 'says', 'she', 'loves', 'you', 'and', 'you', 'know', 'that', "can't", 'be', 'bad', 'she', 'loves', 'you', 'and', 'you', 'know', 'you', 'should', 'be', 'glad', 'she', 'said', 'you', 'hurt', 'her', 'so', 'she', 'almost', 'lost', 'her', 'mind', 'but', 'now', 'she', 'says', 'she', 'knows', "you're", 'not', 'the', 'hurting', 'kind', 'she', 'says', 'she', 'loves', 'you', 'and', 'you', 'know', 'that', "can't", 'be', 'bad', 'she', 'loves', 'you', 'and', 'you', 'know', 'you', 'should', 'be', 'glad', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah', 'with', 'a', 'love', 'like', 'that', 'you', 'know', 'you', 'should', 'be', 'glad', 'you', 'know', "it's", 'up', 'to', 'you', 'i', 'think', "it's", 'only', 'fair', 'pride', 'can', 'hurt', 'you', 'too', 'so', 'apologize', 'to', 'her', 'because', 'she', 'loves', 'you', 'and', 'you', 'know', 'that', "can't", 'be', 'bad', 'she', 'loves', 'you', 'and', 'you', 'know', 'you', 'should', 'be', 'glad', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah', 'with', 'a', 'love', 'like', 'that', 'you', 'know', 'you', 'should', 'be', 'glad', 'with', 'a', 'love', 'like', 'that', 'you', 'know', 'you', 'should', 'be', 'glad', 'with', 'a', 'love', 'like', 'that', 'you', 'know', 'you', 'should', 'be', 'glad', 'yeah', 'yeah', 'yeah', 'yeah', 'yeah', 'yeah']
            
beatles = lyrics_to_frequencies(she_loves_you)

def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)

def words_often (freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result

print(words_often(beatles, 5))