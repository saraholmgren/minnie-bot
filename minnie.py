#!/usr/bin/python
import re,random
from random import randint,choice

words = []
h = []
ass = {}
sentence_start = []

def read_in(): #get words from external files
    try:
        global file
        global file_starters
        file = open('words.txt','r+')
        filestr = file.read().split(" ")
        for x in filestr:
            words.append(x)
        print('read file (words.txt)')
        file.close()

        file_starters = open('starters.txt','r+')
        filestring = file_starters.read().split(" ")
        for x in filestring:
            sentence_start.append(x)
        print('read file (starters.txt)\n')
        file_starters.close()
    except BaseException as error:
        print(error)
read_in()

def get(): #get words to write
    global sentence_start
    readsentence = input("input: ")
    low = readsentence.lower()
    h = re.sub("[^\w]", " ",  low).split()
    print(type(h))
    try:
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
    except BaseException as error:
        print(error)
get()

def writeout(): #write out any new words by .truncate() and overwrite existing file
    try:
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
    except BaseException as error:
        print(error)
writeout()

def wordass(): #remove punctuation and append words into a dict of word associations
    try:
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
    except BaseException as error:
        print(error)
    print(ass)
wordass()
