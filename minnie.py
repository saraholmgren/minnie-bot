#!/usr/bin/python
import re,random
from random import randint,choice

words = []
h = []
ass = {}
sentence_start = []
writing = []

def read_in(): #get words from external files
    global file
    global file_starters
    try:
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

def appendfiles(): #get words to write
    try:
        for x in writing:
            if x in words:
                pass
            if x not in words:
                words.append(x)
        words.pop(0)
        
        s = writing[0] # 's' <str>
        ss = s.split(" ") # 'ss' <list>
        for x in ss:
            if x in writing:
                pass
            if x not in sentence_start:
                sentence_start.append(x)
        sentence_start.pop(0)
    except BaseException as error:
        print(error)

def writeout(): #write out any new words by .truncate() and overwrite existing file
    try:
        r = ''
        file = open('words.txt','r+')
        print(words,'you are writing out this to words.txt')
        file.truncate()
        r = ' '.join(words)
        file.write(r)
        file.close()

        k = ''
        file_starters = open('starters.txt','r+')
        print(sentence_start,'you are writing out this to starters.txt')
        file_starters.truncate()
        k = ' '.join(sentence_start)
        file_starters.write(k)
        file_starters.close()
    except BaseException as error:
        print(error)

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

def speak(getwords):
    global writing
    low = getwords.lower()
    writing = re.sub("[^\w]", " ",  low).split()
    appendfiles()
    writeout()
    wordass()
