import ebooklib
from ebooklib import epub

import os

# Path ermitteln
path = os.path.join('Archive')
files = os.listdir(path)
f = []

for i in range(0,len(files)):
    src = os.path.join(path,files[i])
    # Whitespace
    f.append(files[i].replace(' ',''))
    # print(f[i])
    f[i]=f[i].replace('(','')
    f[i]=f[i].replace(')','')
    f[i]=f[i].replace("'",'')
    f[i]=f[i].replace('-','')
    f[i]=f[i].replace(',','')
    f[i]=f[i].replace('J.K.','JK')
    # print(f[i])
    dst = os.path.join(path,f[i])
    os.rename(src,dst)
    book = epub.read_epub(dst)
    # print(book)
    # print(book.get_metadata('DC','identifier'))'
    # print(book.get_metadata('DC','title'))
    # print(book.get_metadata('DC','creator'))
    # print(book.get_metadata('DC','language'))
    
    path = os.path.join('data')
    if os.path.exists(path):
        with open(os.path.join(path,str(i)+'.txt'),'w',encoding='utf-8') as f:
            title = book.get_metadata('DC','title')
            creator = book.get_metadata('DC','creator')
            meta = '<title>' + str(title[0]) + '</title>' + '<creator>' + str(creator[0]) + '</creator>'   
            f.write(meta)

    # for item in book.get_items():
    #     if item.get_type() == ebooklib.ITEM_DOCUMENT and os.path.exists(path):
    #         # print(item.get_content().decode('utf-8'))
    #         with open(os.path.join(path,str(i)+'.txt'),'a',encoding='utf-8') as f:
    #             content = item.get_body_content().decode('utf-8')
    #             f.write(content)
