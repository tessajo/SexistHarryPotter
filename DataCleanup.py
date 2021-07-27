import os
from bs4 import BeautifulSoup as bs
from bs4.builder import HTML 
import re
import json
from nltk.downloader import update

from textblob_de import TextBlobDE as tb
import nltk

def cleanData(text): # TODO
    # Namen bereinigen
    # Lord Voldemort. Tom Riddle
    text = re.sub("[\s,.!?]Vol[\s,.!?]|[\s,.!?]Vodlemort[\s,.!?]|[\s,.!?]Voldemord[\s,.!?]|[\s,.!?]Voldy[\s,.!?]"," Voldemort ",text)
    # Harry Potter
    text = re.sub("[\s,.!?]Potter[\s,.!?]|[\s,.!?]POTTER[\s,.!?]|[\s,.!?]Potters[\s,.!?]"," Potter ",text)
    text = re.sub("[\s,.!?]Harry[\s,.!?]|[\s,.!?]Harrys[\s,.!?]|[\s,.!?]Arry[\s,.!?]|[\s,.!?]HARRY[\s,.!?]|[\s,.!?]UNDESIRABLE[\s,.!?]|[\s,.!?]Undesirable[\s,.!?]|[\s,.!?]'arry[\s,.!?]|[\s,.!?]Harryk[\s,.!?]"," Harry ",text)
    text = re.sub("[\s,.!?]JAMES[\s,.!?]"," James ",text)
    text = re.sub("[\s,.!?]LILY[\s,.!?]"," Lily ",text)
    # Albus Dumbledore
    text = re.sub("[\s,.!?]Albus[\s,.!?]|[\s,.!?]ALBUS[\s,.!?]|[\s,.!?]Percival[\s,.!?]|[\s,.!?]Al[\s,.!?]|[\s,.!?]Ablus[\s,.!?]"," Albus ",text)
    text = re.sub("[\s,.!?]Dumbledore[\s,.!?]|[\s,.!?]DUMBLEDORE[\s,.!?]|[\s,.!?]Dumbledores[\s,.!?]"," Dumbledore ",text)
    # Dursleys
    text = re.sub("[\s,.!?]Dursley[\s,.!?]|[\s,.!?]Dursleys[\s,.!?]|[\s,.!?]DURSLEYS[\s,.!?]"," Dursley ",text)
    text = re.sub("[\s,.!?]Duddy[\s,.!?]"," Dudley ",text)
    text = re.sub("[\s,.!?]Tuney[\s,.!?]"," Petunia ",text)
    # Nymphadora Tonks
    text = re.sub("[\s,.!?]Dora[\s,.!?]"," Nymphadora ",text)
    # Hermione Granger
    text = re.sub("[\s,.!?]HERMIONE[\s,.!?]"," Hermione ",text)
    # Dobby
    text = re.sub("[\s,.!?]DOB[\s,.!?]|[\s,.!?]DOBBY[\s,.!?]"," Dobby ",text)
    # Weasleys
    text = re.sub("[\s,.!?]Georgie[\s,.!?]|[\s,.!?]George-ish[\s,.!?]"," George ",text)
    text = re.sub("[\s,.!?]Ginevra[\s,.!?]"," Ginny ",text)
    text = re.sub("[\s,.!?]Perce[\s,.!?]"," Percy ",text)
    # Delacour
    text = re.sub("[\s,.!?]Delacours[\s,.!?]"," Delacour ",text)
    # Rubeus Hagrid
    text = re.sub("[\s,.!?]HAGRID[\s,.!?]|[\s,.!?]HAGGER[\s,.!?]"," Hagrid ",text)
    # Gregorovitch
    text = re.sub("[\s,.!?]Gregorowitch[\s,.!?]"," Gregorovitch ",text)
    # Fenrir Greyback
    text = re.sub("[\s,.!?]Fenrit[\s,.!?]"," Fenrir ",text)
    # Gellert Grindelwald
    text = re.sub("[\s,.!?]Grindelvald[\s,.!?]"," Grindelwald ",text)
    # Spitznamen
    text = re.sub("[\s,.!?]Padfoot[\s,.!?]"," Sirius ",text)
    text = re.sub("[\s,.!?]Wormy[\s,.!?]"," Peter ",text)
    text = re.sub("[\s,.!?]Moony[\s,.!?]"," Remus ",text)
    text = re.sub("[\s,.!?]Stag[\s,.!?]|[\s,.!?]Prongs[\s,.!?]"," James ",text)
    # Malfoy
    text = re.sub("[\s,.!?]Cissy[\s,.!?]"," Narcissa ",text)
    text = re.sub("[\s,.!?]MALFOY[\s,.!?]"," Malfoy ",text)
    # Severus Snape
    text = re.sub("[\s,.!?]SEVERUS[\s,.!?]|[\s,.!?]Sev[\s,.!?]"," Severus ",text)
    text = re.sub("[\s,.!?]Sanpe[\s,.!?]"," Snape ",text)
    # Regulus Black
    text = re.sub("[\s,.!?]Reg[\s,.!?]"," Regulus ",text)
    # Xenophilius Lovegood
    text = re.sub("[\s,.!?]Xeno[\s,.!?]"," Xenophilius ",text)
    # Todesser
    text = re.sub("[\s,.!?]ALECTO[\s,.!?]"," Alecto ",text)
    text = re.sub("[\s,.!?]ROOKWOOD[\s,.!?]"," Rookwood ",text)
    # Zentauren
    text = re.sub("[\s,.!?]BANE[\s,.!?]"," Bane ",text)
    # Allgemein
    text = re.sub("[\s,.!?]GENTLEMEN[\s,.!?]"," gentlemen ",text)
    text = re.sub("[\s,.!?]LADIES[\s,.!?]"," ladies ",text)
    # Colin Creevey
    text = re.sub("[\s,.!?]Colon[\s,.!?]"," Colin ",text)
    # Rose Potter
    text = re.sub("[\s,.!?]Roses[\s,.!?]|[\s,.!?]Rosie[\s,.!?]"," Rose ",text)
    return text

def getNamedEntities(text):
    # Named Entities ermitteln
    # Tokens erzeugen
    tokens = nltk.word_tokenize(text)
    # Part of Speech Tags erzeugen
    tagged = nltk.pos_tag(tokens)
    # Named Entities aus POS Tags ermitteln
    entities = nltk.chunk.ne_chunk(tagged)
    return entities

def getTextfromHTML():
    # Dateidirectory auslesen. Iterieren über Dateien
    files = os.listdir('Data\RAW')
    for i in range(0,len(files)):
        # Dateien auslesen
        with open(os.path.join('Data','RAW',files[i]),'r',encoding='utf-8') as f:
            raw = f.read()
        # HTML Parser initialisieren
        soup = bs(raw,'html.parser')
        # Text aus HTML auslesen
        rawtext = soup.get_text()
        cleantext = cleanData(rawtext)
        # Bereinigten Text in Datei schreiben
        with open(os.path.join('Data','REFINED',str(i)+'.txt'),'w',encoding='utf-8') as f:
            f.write(cleantext)

def getNames():
    # Dateidirectory auslesen. Iterieren über Dateien
    files = os.listdir('Data\REFINED')
    # Dictionaries initialisieren
    adjectives = {}
    adverbs = {}
    names = {}
    # Ausnahmen auslesen
    with open(os.path.join('Data','pos','exceptions.json'),'r',encoding='utf-8') as f:
            text = f.read().replace('\xad','')
            d = json.loads(text)
            ex = d.keys()
    for i in range(0,len(files)):
        # Dateien auslesen
        with open(os.path.join('Data','REFINED',files[i]),'r',encoding='utf-8') as f:
            text = f.read().replace('\xad','') # TODO test this!
        # Named Entities erzeugen
        entities = getNamedEntities(text)
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
    files = os.listdir('Data\REFINED')
    for i in range(0,len(files)):
        with open(os.path.join('Data','REFINED',str(i)+'.txt'),'r',encoding='utf-8') as f:
            text = f.read()

        entities = getNamedEntities(text)
        
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
    n = {}
    with open(os.path.join('Data','pos','names.json'),'r',encoding='utf-8') as f:
        content = f.read()
        n = json.loads(content)
        names = n.keys()

    print(names)
    # files = os.listdir('Data\REFINED')
    # for i in range(0,1): # len(files)):
    #     with open(os.path.join('Data','REFINED',files[i]),'r',encoding='utf-8') as f:
    #         text = f.readlines()
    #     # print(text)
    #     i = 1
    #     for line in text:
    #         # print(line)
    #         if re.findall('Potter',line):
    #             print(i)
    #             i +=1
    #             print(line)


# Ausführen von Funktionen

# cleanData()
getTextfromHTML()
getNames()
# getDescriptives()
getSentences()