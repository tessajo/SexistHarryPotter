import evalFunctions as ef
unigram=[]
seq = ["Harry"] #,"d","never","believed","he","would","meet","a","boy","he","hated","more","than","Dudley"]
lseq = len(seq)-1
i=0
for word in seq:
    print(word)
    ef.createWordMatrix(word,seq,lseq,unigram,i)
    i +=1


def getSentences():
    # Namen auslesen

    n = {}
    names = []
    with open(os.path.join('Data','pos','names.json'),'r',encoding='utf-8') as f:
        content = f.read().replace('\xad','')
    n = json.loads(content)
    for key in n.keys():
        names.append(key)


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
            adverbs.append(key)
    # Alle Texte auslesen
    with open(os.path.join('Data','REFINED','master.txt'),'r',encoding='utf-8') as f:
        content = f.read().replace('\xad','') 

    sentences = nltk.sent_tokenize(content,language='english')
    
    
    
    
    
    if not os.path.exists(os.path.join('Data','RESULTS','allsentences.txt')) and not os.path.exists(os.path.join('Data','RESULTS','sentenceswithnames.txt')):
        with open(os.path.join('Data','RESULTS','sentenceswithnames.txt'),'w',encoding='utf-8') as f:
            f.write('')        
        with open(os.path.join('Data','RESULTS','allsentences.txt'),'w',encoding='utf-8') as f:
            f.write('')
    for s in sentences:
        res = s + '\n\n'
        if re.search(names[0],s) and (re.search(adjectives[0],s) or re.search(adverbs[0],s)):
            with open(os.path.join('Data','RESULTS','sentenceswithnames.txt'),'a',encoding='utf-8') as f:
                f.write(res) 
        with open(os.path.join('Data','RESULTS','allsentences.txt'),'a',encoding='utf-8') as f:
            f.write(res)
