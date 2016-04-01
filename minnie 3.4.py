#!/usr/bin/python
import re,random
from random import randint
words = []
h = []
ass = {}
def read_in():
    global file
    file = open('words.txt','r+')
    filestr = file.read().split(" ")
    for x in filestr:
        words.append(x)
    file.close()
read_in()

def get():
    readsentence = input(": ")
    low = readsentence.lower()
    h = re.sub("[^\w]", " ",  low).split()
    for x in h:
        if x in words:
            pass
        if x not in words:
            words.append(x)
    words.pop(0)
get()

def writeout():
    r = ''
    file = open('words.txt','r+')
    file.truncate()
    r = ' '.join(words)
    file.write(r)
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
