#!/usr/bin/python
import re,json
from random import randint,choice
from collections import defaultdict

words = []
h = []
ass = {}
sentence_start = []
writing = []

def read_in(): #get words from external files
    global file
    global file_starters
    global associations
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

        file_associations = open('associations.txt','r+')
        associations = json.loads(file_associations.read())
        print(associations)
    except BaseException as error:
        print(error)
read_in()

def appendfiles(): #get words to write
    try:
        for x in writing:
            if x not in words:
                words.append(x)
        words.pop(0)
        
        s = writing[0] # 's' <str>
        ss = s.split(" ") # 'ss' <list>
        for x in ss:
            if x not in sentence_start:
                sentence_start.append(x)
        sentence_start.pop(0)
    except BaseException as error:
        print(error)

def writeout(): #write out any new words by .truncate() and overwrite existing file
    try:
        r = ''
        file = open('words.txt','r+')
        print(words,"you are writing out this to words.txt\n")
        file.truncate()
        r = ' '.join(words)
        file.write(r)
        file.close()

        k = ''
        file_starters = open('starters.txt','r+')
        print(sentence_start,"you are writing out this to starters.txt\n")
        file_starters.truncate()
        k = ' '.join(sentence_start)
        file_starters.write(k)
        file_starters.close()
    except BaseException as error:
        print(error)

def wordass(): #remove punctuation and append writing into a dict of word associations
    global j
    try:
        for i in range(len(writing)):
            try:
                ass[writing[i]]
            except:
                ass[writing[i]] = []
            if not writing[i][-1] in (".","?","\n","!"):
                try:
                    ass[writing[i]].append(writing[i+1])
                except:
                    pass
    except BaseException as error:
        print(error,"<- an error, fuck!")

    
def speak(getwords):
    global writing
    low = getwords.lower()
    writing = re.sub('[^\w]', ' ',  low).split()
    print("writing",writing)
    wordass()
    appendfiles()
    writeout()
    #writesentence_reply()

def writesentence_reply():
    l = randint(1,50)
    for i in range(0,l):
        x = random.choice(writing)
        print(random.choice(ass[x]))

## dump ##
## outputting = {k:[associations.get(k),ass.get(k)] for k in associations.keys() | ass.keys()}

