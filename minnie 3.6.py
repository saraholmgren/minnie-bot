#!/usr/bin/python
import re,random
from random import randint

words = []
h = []
ass = {}
sentence_start = []

def read_in():
    global file
    global file_starters
    file = open('words.txt','r+')
    filestr = file.read().split(" ")
    for x in filestr:
        words.append(x)
    file.close()

    file_starters = open('starters.txt','r+')
    filestring = file_starters.read().split(" ")
    for x in filestring:
        sentence_start.append(x)
    print(sentence_start,'<< this is sentence start')
    file_starters.close()
read_in()

def get():
    global sentence_start
    readsentence = input("input: ")
    low = readsentence.lower()
    h = re.sub("[^\w]", " ",  low).split()
    for x in h:
        if x in words:
            pass
        if x not in words:
            words.append(x)
    words.pop(0)

    s = h[0] # 's' <str>
    ss = s.split(" ") # 'ss' <list>
    for x in ss:
        if x in sentence_start:
            pass
        if x not in sentence_start:
            sentence_start.append(x)
    sentence_start.pop(0)
get()

def writeout():
    r = ''
    file = open('words.txt','r+')
    file.truncate()
    r = ' '.join(words)
    file.write(r)
    file.close()

    k = ''
    file_starters = open('starters.txt','r+')
    file_starters.truncate()
    k = ' '.join(sentence_start)
    file_starters.write(k)
    file_starters.close()
writeout()

def wordass(): #ty max
    for i in range(len(words)):
        try:
            ass[words[i]]
        except:
            ass[words[i]] = []
        if not words[i][-1] in (".","?","\n","!"):
            try:
                ass[words[i]].append([words[i+1]])
            except:
                pass
    print(ass)
wordass()
