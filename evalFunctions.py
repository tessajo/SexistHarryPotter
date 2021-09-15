import os
import nltk, string, json
from nltk.util import ngrams
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

#Funktionen definieren

punct = ['“','”','–','’','‘','—','…']

# removal-Funktion definieren
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

def createwordmatrix(word,seq,lseq,unigram,i):
    if not lseq==i:
        createwordmatrix(word,seq,lseq-1,unigram,i)
    if not word==seq[lseq]:
        unigram.append(word)
        unigram.append(seq[lseq])
    return unigram

# ngram-Funktion definieren
def unigram(sents):
    punct = ['“','”','–','’','‘','—','…']
    unigram = [] # nur das Wort wird beachtet
    toktext = []
    for sentence in sents:
        sentence = ''.join([char for char in sentence if (char not in string.punctuation) and (char not in punct)])
        sentence = sentence.lower()
        sequence = nltk.word_tokenize(sentence)
        for word in sequence:
            unigram.append(word)
        toktext.append(sequence)
    return toktext,unigram

def unigrammatrix(sents):
    punct = ['“','”','–','’','‘','—','…']
    unigram = []
    # toktext = []
    for sentence in sents:
        sentence = ''.join([char for char in sentence if (char not in string.punctuation) and (char not in punct)])
        sentence = sentence.lower()
        sequence = nltk.word_tokenize(sentence)
        lseq = len(sequence)-1
        i = 0
        for word in sequence:
            createwordmatrix(word,sequence,lseq,unigram,i)
            i += 1
    return unigram

# ngram-Funktion mit POS definieren
def ngramfilter(unigram,all:bool,names:bool,ad:bool):
    unigramall = ['Harry','Potter']
    unigramnames = []
    unigramad = []
    # POS Tags ermitteln
    sequence = nltk.pos_tag(unigram)
    if all==True:
        for word in sequence:
            if (not word[0]==unigramall[-1] or len(unigramall)==0) and word[1] in ['NN','NNS','NNP','JJ','JJR','JJS','RB','RBR','RBS']: # Nomen, Adverben, Adjektive
                unigramall.append(word[0])
    if names==True: 
        names = []
        with open(os.path.join('Data','pos','names.json'),'r',encoding='utf-8') as f:
            content = f.read().replace('\xad','')
            n = json.loads(content)
            for key in n.keys():
                names.append(key)
        for word in sequence:
            if (not word[0]==unigramall[-1] or len(unigramall)==0) and word[1] in ['JJ','JJR','JJS','RB','RBR','RBS'] or word in names: # Adverben, Adjektive
                unigramnames.append(word[0])
    if ad==True:
        for word in sequence:
            if (not word[0]==unigramall[-1] or len(unigramall)==0) and word[1] in ['JJ','JJR','JJS','RB','RBR','RBS']: # Adverben, Adjektive
                unigramad.append(word[0])
    return unigramall,unigramnames,unigramad

def initngrams(unigram):
    # N-Grams
    bigram = [] # Kontext (2 Worte) wird beachtet
    trigram = []
    fourgram = []
    fivegram = []
    sixgram = []

    # Filterwerte ermitteln
    fv = getfiltervalues(1,0,0)

    # n-Grame erstellen 
    bigram.extend(list(ngrams(unigram, 2)))
    trigram.extend(list(ngrams(unigram, 3)))
    fourgram.extend(list(ngrams(unigram, 4)))
    fivegram.extend(list(ngrams(unigram, 5)))
    sixgram.extend(list(ngrams(unigram, 6)))
    
    unigram = removal(unigram,fv)
    bigram = removal(bigram,fv)
    trigram = removal(trigram,fv)
    fourgram = removal(fourgram,fv)
    fivegram = removal(fivegram,fv)
    sixgram = removal(sixgram,fv)
    
    freq_uni = nltk.FreqDist(unigram)
    freq_bi = nltk.FreqDist(bigram)
    freq_tri = nltk.FreqDist(trigram)
    freq_four = nltk.FreqDist(fourgram)
    freq_five = nltk.FreqDist(fivegram)
    freq_six = nltk.FreqDist(sixgram)

    # print('freq_uni',freq_uni.most_common(100),'\n')
    # print('freq_bi',freq_bi.most_common(20),'\n')
    # print('freq_tri',freq_tri.most_common(20),'\n')
    # print('freq_four',freq_four.most_common(20),'\n')
    # print('freq_five',freq_five.most_common(20),'\n')
    # print('freq_six',freq_six.most_common(20),'\n')
    return freq_uni

def getwordfrequency(unigram): # TODO
    x = []
    y = []
    print(unigram)
    # Ergebnisse
    print('freq_uni',unigram.most_common(100),'\n')
    tuple_gram = unigram.most_common(100)
    for tuple in tuple_gram:
        print(tuple,tuple[0],tuple[1])
        if int(tuple[1])>30:
            x.append(tuple[0]) 
            y.append(tuple[1])
    
    fig = plt.figure(figsize = (20,5))
    plt.bar(x,y)
    plt.title("Worthäufigkeiten", loc = 'left')
    plt.xlabel("Wort")
    plt.ylabel("Frequenz")
    plt.xticks(rotation=90)
    plt.show()

def getfiltervalues(n,adv,adj):
    names = []
    adverbs = []
    adjectives = []
    res = []
    if n==1:
        with open(os.path.join('Data','pos','names.json'),'r',encoding='utf-8') as f:
            content = f.read().replace('\xad','')
        n = json.loads(content)
        for key in n.keys():
            names.append(key)
    if adv==1:
        with open(os.path.join('Data','pos','adverb.json'),'r',encoding='utf-8') as f:
            content = f.read().replace('\xad','')
        n = json.loads(content)
        for key in n.keys():
            adverbs.append(key)
    if adj==1:
        with open(os.path.join('Data','pos','adjectives.json'),'r',encoding='utf-8') as f:
            content = f.read().replace('\xad','')
        n = json.loads(content)
        for key in n.keys():
            adjectives.append(key)
    res.extend(names)
    res.extend(adverbs)
    res.extend(adjectives)  
    return res