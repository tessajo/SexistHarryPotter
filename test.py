import evalFunctions as ef
unigram=[]
seq = ["Harry"] #,"d","never","believed","he","would","meet","a","boy","he","hated","more","than","Dudley"]
lseq = len(seq)-1
i=0
for word in seq:
    print(word)
    ef.createWordMatrix(word,seq,lseq,unigram,i)
    i +=1