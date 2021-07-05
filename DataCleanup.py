import os
from bs4 import BeautifulSoup as bs
from bs4.builder import HTML 
import re
import json
from nltk.downloader import update

from textblob_de import TextBlobDE as tb
import nltk

def cleanData():
    files = os.listdir('Data\RAW')
    for i in range(0,len(files)):
        with open(os.path.join('Data','RAW',str(i)+'.txt'),'r',encoding='utf-8') as f:
            raw = f.read()
        soup = bs(raw,'html.parser')
        clean = soup.get_text()
        # print(clean)
        with open(os.path.join('Data','REFINED',str(i)+'.txt'),'w',encoding='utf-8') as f:
            f.write(clean)

def getNames():
    files = os.listdir('Data\RAW')
    for i in range(0,1):
        with open(os.path.join('Data','REFINED',str(i)+'.txt'),'r',encoding='utf-8') as f:
            text = f.read()
        blob = tb(text)
        print(blob.tokenize())

def nltkgetNames():
    files = os.listdir('Data\REFINED')
    for i in range(0,len(files)):
        with open(os.path.join('Data','REFINED',str(i)+'.txt'),'r',encoding='utf-8') as f:
            text = f.read()

        tokens = nltk.word_tokenize(text)
        tagged = nltk.pos_tag(tokens)
        entities = nltk.chunk.ne_chunk(tagged)
        
        adjectives = {}
        adverbs = {}
        names = {}
        for e in entities:
            if 'JJ' in e:
                key = e[0]
                value = e[1]
                adjectives.update({key:value})
            if 'JJS' in e:
                key = e[0]
                value = e[1]
                adjectives.update({key:value})
            if 'JJC' in e:
                key = e[0]
                value = e[1]
                adjectives.update({key:value})
            if 'RB' in e:
                key = e[0]
                value = e[1]
                adverbs.update({key:value})
            if 'RBR' in e:
                key = e[0]
                value = e[1]
                adverbs.update({key:value})
            if 'RBS' in e:
                key = e[0]
                value = e[1]
                adverbs.update({key:value})
            if hasattr(e,'label'):
                key = e[0][0]
                value = e.label()
                names.update({key:value})
        
        path = os.path.join('Data','pos')
        with open(os.path.join(path,'adjectives.json'),'w',encoding='utf-8') as f:
            json.dump(adjectives,f,indent=4,ensure_ascii=False)
            print('json befüllt')
        with open(os.path.join(path,'adverbs.json'),'w',encoding='utf-8') as f:
            json.dump(adverbs,f,indent=4,ensure_ascii=False)
            print('json befüllt')
        with open(os.path.join(path,'names.json'),'w',encoding='utf-8') as f:
            json.dump(names,f,indent=4,ensure_ascii=False)
            print('json befüllt')

def getDescriptives():
    files = os.listdir('Data\REFINED')
    for i in range(0,len(files)):
        with open(os.path.join('Data','REFINED',str(i)+'.txt'),'r',encoding='utf-8') as f:
            text = f.read()

        tokens = nltk.word_tokenize(text)
        tagged = nltk.pos_tag(tokens)
        entities = nltk.chunk.ne_chunk(tagged)
        
        descriptors = {}
        for e in entities:
            l = []
            if 'JJ' in e:
                key = e[0]
                descriptors.update({key:0})
            if 'JJS' in e:
                key = e[0]
                descriptors.update({key:0})
            if 'JJC' in e:
                key = e[0]
                descriptors.update({key:0})
            if 'RB' in e:
                key = e[0]
                descriptors.update({key:0})
            if 'RBR' in e:
                key = e[0]
                descriptors.update({key:0})
            if 'RBS' in e:
                key = e[0]
                descriptors.update({key:0})
            # if hasattr(e,'label'):
            #     key = e[0][0]
            #     value = e.label()
            #     l.append(key)
            #     l.append(value)S
            #     names.update({key:value})
        
        path = os.path.join('Data','pos')
        with open(os.path.join(path,'isdescriptive.json'),'w',encoding='utf-8') as f:
            json.dump(descriptors,f,indent=4,ensure_ascii=False)
            print('json befüllt')
        # with open(os.path.join(path,'names.json'),'w',encoding='utf-8') as f:
        #     json.dump(names,f,indent=4,ensure_ascii=False)
        #     print('json befüllt')

def getSentences(entities):
    files = os.listdir('Data\REFINED')
    for i in range(0,1):
        with open(os.path.join('Data','REFINED',str(i)+'.txt'),'r',encoding='utf-8') as f:
            text = f.read()
        for line in text:
            re.search()



# cleanData()
# getNames()
# nltkgetNames()
getDescriptives()