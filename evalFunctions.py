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

def createWordMatrix(word,seq,lseq,unigram,i):
    if not lseq==i:
        createWordMatrix(word,seq,lseq-1,unigram,i)
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

def unigramMatrix(sents):
    punct = ['“','”','–','’','‘','—','…']
    unigram = []
    l_names = getFilterValues(1,0,0,0,0)
    for sentence in sents:
        sentence = ''.join([char for char in sentence if (char not in string.punctuation) and (char not in punct)])
        sentence = sentence.lower()
        sequence = nltk.word_tokenize(sentence)
        lseq = len(sequence)-1
        i = 0
        for word in sequence:
            print(word)
            if word in l_names:
                print(word)
                createWordMatrix(word,sequence,lseq,unigram,i)
            i += 1
    return unigram

# ngram-Funktion mit POS definieren
def ngramFilter(unigram,all:bool,names:bool,ad:bool):
    unigramall = []
    unigramnames = []
    unigramad = []
    # POS Tags ermitteln
    sequence = nltk.pos_tag(unigram)
    if all==True:
        for word in sequence:
            if word[1] in ['NN','NNS','NNP','JJ','JJR','JJS','RB','RBR','RBS']: # Nomen, Adverben, Adjektive
                if len(unigramall)==0 or word[0]!=unigramall[-1]:
                    unigramall.append(word[0])
    if names==True: 
        names = []
        with open(os.path.join('Data','pos','names.json'),'r',encoding='utf-8') as f:
            content = f.read().replace('\xad','')
            n = json.loads(content)
            for key in n.keys():
                names.append(key)
        for word in sequence:
            if word[0] in names: # Adverben, Adjektive
                if len(unigramnames)==0 or word[0]!=unigramnames[-1]:
                    unigramnames.append(word[0])
    if ad==True:
        for word in sequence:
            if word[1] in ['JJ','JJR','JJS','RB','RBR','RBS']: # Adverben, Adjektive
                if len(unigramad)==0 or word[0]!=unigramad[-1]:
                    unigramad.append(word[0])
    return unigramall,unigramnames,unigramad

def initNgrams(unigram):
    # N-Grams
    bigram = [] # Kontext (2 Worte) wird beachtet
    trigram = []
    fourgram = []
    fivegram = []
    sixgram = []

    # Filterwerte ermitteln
    fv = getFilterValues(1,0,0,0,0)

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
    return freq_uni,bigram

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
    # print('freq_uni',unigram.most_common(100),'\n')
    tuple_gram = unigram.most_common(100)
    for tuple in tuple_gram:
        # if int(tuple[1])>30:
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
    plt.title("Worthäufigkeiten")
    plt.xlabel("Wort")
    plt.ylabel("Frequenz")
    plt.xticks(rotation=90)
    # plt.figlegend([1,2,3,4],labels = legend,labelcolor=[c_noun,c_adv,c_adj,c_none]) # TODO Legende definieren
    plt.show()

def getFilterValues(n:bool,adv:bool,adj:bool,female_n:bool,male_n:bool):
    # List var should have different name to boolean
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
    if adv==1:
        with open(os.path.join('Data','pos','adverbs.json'),'r',encoding='utf-8') as f:
            content = f.read().replace('\xad','')
        n = json.loads(content)
        for key in n.keys():
            adverbs.append(key.lower())
    if adj==1:
        with open(os.path.join('Data','pos','adjectives.json'),'r',encoding='utf-8') as f:
            content = f.read().replace('\xad','')
        n = json.loads(content)
        for key in n.keys():
            adjectives.append(key.lower())
    if female_n==1:
        with open(os.path.join('Data','pos','female.json'),'r',encoding='utf-8') as f:
            content = f.read().replace('\xad','')
        n = json.loads(content)
        for key in n.keys():
            female.append(key.lower())
    if male_n==1:
        with open(os.path.join('Data','pos','male.json'),'r',encoding='utf-8') as f:
            content = f.read().replace('\xad','')
        n = json.loads(content)
        for key in n.keys():
            male.append(key.lower())
    return names,adverbs,adjectives,female,male