import os
from bs4 import BeautifulSoup as bs
from bs4.builder import HTML 
import re
import json
import string
from nltk.downloader import update
import nltk

import DataCleanup as dc

def getNames():
    # Dictionaries initialisieren
    adjectives = {}
    adverbs = {}
    names = {}
    # Ausnahmen auslesen
    with open(os.path.join('Data','pos','exceptions.json'),'r',encoding='utf-8') as f:
            text = f.read().replace('\xad','')
            d = json.loads(text)
            ex = d.keys()
    # # Dateien auslesen
    with open(os.path.join('Data','REFINED','master.txt'),'r',encoding='utf-8') as f:
        text = f.read().replace('\xad','')
        # Named Entities erzeugen
        entities = dc.getNamedEntities(text)
        # Über Entities iterieren, um Entities den Dictionaries zuzuordnen
        for e in entities:
            # Adjektiv
            if 'JJ' in e: 
                key = e[0]
                value = e[1]
                adjectives.update({key:value})
            # Adjektiv
            if 'JJS' in e:
                key = e[0]
                value = e[1]
                adjectives.update({key:value})
            # Adjektiv
            if 'JJR' in e:
                key = e[0]
                value = e[1]
                adjectives.update({key:value})
            # Adverb
            if 'RB' in e: 
                key = e[0]
                value = e[1]
                adverbs.update({key:value})
            # Adverb
            if 'RBR' in e:
                key = e[0]
                value = e[1]
                adverbs.update({key:value})
            # Adverb
            if 'RBS' in e:
                key = e[0]
                value = e[1]
                adverbs.update({key:value})
            # Namen
            if hasattr(e,'label') and e[0][0] not in ex:
                key = e[0][0]
                value = e.label()
                names.update({key:value})
        print(names)
        # JSON-Dateien befüllen
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
    # JSON-Dateien, die binär darstellen, ob gefundene Adjektive und Adverbe deskriptiv sind
    with open(os.path.join('Data','REFINED','master.txt'),'r',encoding='utf-8') as f:
        text = f.read().replace('\xad','')

    entities = dc.getNamedEntities(text)
    
    descriptors = {}
    for e in entities:
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
    
    path = os.path.join('Data','pos')
    with open(os.path.join(path,'isdescriptive.json'),'w',encoding='utf-8') as f:
        json.dump(descriptors,f,indent=4,ensure_ascii=False)
        print('json befüllt')

def getSentences():
    # Namen auslesen
    n = {}
    names = []
    with open(os.path.join('Data','pos','names.json'),'r',encoding='utf-8') as f:
        content = f.read().replace('\xad','') # \xad = optional -
    n = json.loads(content)
    for key in n.keys():
        names.append(key.lower())
    '''
    adjectives = []
    with open(os.path.join('Data','pos','adjectives.json'),'r',encoding='utf-8') as f:
        content = f.read().replace('\xad','')
        n = json.loads(content)
        for key in n.keys():
            adjectives.append(key)
    adverbs = []
    with open(os.path.join('Data','pos','adverbs.json'),'r',encoding='utf-8') as f:
        content = f.read().replace('\xad','')
        n = json.loads(content)
        for key in n.keys():
            adverbs.append(key) '''
    # Alle Texte auslesen
    with open(os.path.join('Data','REFINED','master.txt'),'r',encoding='utf-8') as f:
        content = f.read().replace('\xad','') 
    sentences = nltk.sent_tokenize(content,language='english')
    filtered_text = ''
    text = ''
    if not os.path.exists(os.path.join('Data','RESULTS','allsentences.txt')) and not os.path.exists(os.path.join('Data','RESULTS','sentenceswithnames.txt')):
        with open(os.path.join('Data','RESULTS','sentenceswithnames.txt'),'w',encoding='utf-8') as f:
            f.write('')        
        with open(os.path.join('Data','RESULTS','allsentences.txt'),'w',encoding='utf-8') as f:
            f.write('')
    for sentence in sentences:
        seq = nltk.word_tokenize(sentence.lower())
        l_seq = len(seq)-1
        filtered_text += findWordInSentence(sentence,seq,names,l_seq)
        text += sentence + '\n'
    with open(os.path.join('Data','RESULTS','sentenceswithnames.txt'),'a',encoding='utf-8') as f:
        f.write(filtered_text) 
    with open(os.path.join('Data','RESULTS','allsentences.txt'),'a',encoding='utf-8') as f:
        f.write(text)

def findWordInSentence(sentence,seq,comparison:list,i):
    if seq[i] in comparison:
        return sentence
    elif i>0:
        return findWordInSentence(sentence,seq,comparison,i-1)
    else:
        return ''

getSentences()