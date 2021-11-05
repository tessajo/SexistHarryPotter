import sys
import os
import nltk, string, json
from nltk.util import ngrams
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

# Removal-Funktion
def removal(x,fv):
    stop_words = set(stopwords.words('english'))
    # Stopwörter entfernen
    res = []
    for pair in x:
        l = len(pair)
        count = 0
        for word in pair:
            if word in stop_words:
                count = count or 0
            else:
                count = count or 1
        if count==1:
            for word in pair:
                if word in fv or len(fv)==0:
                    count = count or 1
        if count==1:  
            res.append(pair)
    return res

# Rekursive Matrix-Funktion
def createWordMatrix(word,seq,lseq,unigram,i):
    if not lseq==i:
        createWordMatrix(word,seq,lseq-1,unigram,i)
    if not word==seq[lseq]:
        unigram.append(word)
        unigram.append(seq[lseq])
    return unigram

# Erstellen eines Unigrams und ein tokenisierter Text
def unigram(sents):
    punct = ['“','”','–','’','‘','—','…']
    unigram = []
    toktext = []
    for sentence in sents:
        sentence = ''.join([char for char in sentence if (char not in string.punctuation) and (char not in punct)])
        sentence = sentence.lower()
        sequence = nltk.word_tokenize(sentence)
        for word in sequence:
            unigram.append(word)
        toktext.append(sequence)
    return toktext,unigram

# Erstellung eines Matrix-Unigrams
def unigramMatrix(sents:list):
    unigram = []
    l_names, adverbs, adjectives, female, male, res = getFilterValues(1,0,0,0,0)
    for sentence in sents:
        sequence = nltk.word_tokenize(sentence)
        lseq = len(sequence)-1
        i = 0
        for word in sequence:
            if word in l_names:
                createWordMatrix(word,sequence,lseq,unigram,i)
            i += 1
    return unigram

def ngramFilter(unigram):
    unigramall = []
    # POS Tags ermitteln
    sequence = nltk.pos_tag(unigram)
    names = []
    with open(os.path.join('Data','pos','names.json'),'r',encoding='utf-8') as f:
        content = f.read().replace('\xad','')
        n = json.loads(content)
    for key in n.keys():
        names.append(key)
    for word in sequence:
        if word[1] in ['JJ','JJR','JJS','RB','RBR','RBS'] or word[0] in names: # Nomen, Adverben, Adjektive
            if len(unigramall)==0 or word[0]!=unigramall[-1]:
                unigramall.append(word[0])
    return unigramall

def initNgrams(unigram):
    # Variable erstellen
    bigram = []
    # Filterwerte ermitteln
    fv = getFilterValues(1,0,0,0,0)
    # n-Grame erstellen 
    bigram.extend(list(ngrams(unigram, 2)))
    # Removal-Funktion anwenden
    unigram = removal(unigram,fv)
    # FreqDist berechnen
    freq_uni = nltk.FreqDist(unigram)
    freq_bi = nltk.FreqDist(bigram)
    len_bi = len(freq_bi)
    return freq_uni,freq_bi.most_common(len_bi)

def getWordFrequency(unigram): # TODO
    # Variablendeklaration
    x = []
    y = []
    color = []
    gram_pos = nltk.pos_tag(unigram)
    counter = 0
    c_noun = "green" 
    c_adv = "yellow"
    c_adj = "red"
    c_none = "blue"
    legend = ['Nomen','Adverb','Adjektiv','Andere']
    # Ergebnisse
    tuple_gram = unigram.most_common(100)
    for tuple in tuple_gram:
        x.append(tuple[0]) 
        y.append(tuple[1])
        if gram_pos[counter][1] in ['NN','NNS','NNP']:
            color.append(c_noun)
        elif gram_pos[counter][1] in ['JJ','JJR','JJS']:
            color.append(c_adv)
        elif gram_pos[counter][1] in ['RB','RBR','RBS']:
            color.append(c_adj)
        else:
            color.append(c_none)
        counter += 1
    fig = plt.figure(figsize = (20,5))
    plt.bar(x,y,color = color)
    plt.title("Wordfrequencies")
    plt.xlabel("Word")
    plt.ylabel("Frequency")
    plt.xticks(rotation=90)
    plt.show()

# Funktion zum Ermitteln von Filter-werten
def getFilterValues(n:bool,adv:bool,adj:bool,female_n:bool,male_n:bool):
    res = []
    names = []
    adverbs = []
    adjectives = []
    female = []
    male = []
    if n==1:
        with open(os.path.join('Data','pos','names.json'),'r',encoding='utf-8') as f:
            content = f.read().replace('\xad','')
        n = json.loads(content)
        for key in n.keys():
            names.append(key.lower())
    res += names
    if adv==1:
        with open(os.path.join('Data','pos','adverbs.json'),'r',encoding='utf-8') as f:
            content = f.read().replace('\xad','')
        n = json.loads(content)
        for key in n.keys():
            adverbs.append(key.lower())
    res += adverbs
    if adj==1:
        with open(os.path.join('Data','pos','adjectives.json'),'r',encoding='utf-8') as f:
            content = f.read().replace('\xad','')
        n = json.loads(content)
        for key in n.keys():
            adjectives.append(key.lower())
    res += adjectives
    if female_n==1:
        with open(os.path.join('Data','pos','female.json'),'r',encoding='utf-8') as f:
            content = f.read().replace('\xad','')
        n = json.loads(content)
        for key in n.keys():
            female.append(key.lower())
    res += female
    if male_n==1:
        with open(os.path.join('Data','pos','male.json'),'r',encoding='utf-8') as f:
            content = f.read().replace('\xad','')
        n = json.loads(content)
        for key in n.keys():
            male.append(key.lower())
    res += male
    return names, adverbs, adjectives, female, male, res