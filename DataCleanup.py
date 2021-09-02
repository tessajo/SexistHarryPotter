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
    # A
    # Albus Dumbledore
    text = re.sub("ALBUS"," Albus ",text)
    text = re.sub("Percival"," Albus ",text)
    text = re.sub("[\s\n,.!?]*Al[\s\n,.!?]+"," Albus ",text)
    text = re.sub("Ablus"," Albus ",text)
    text = re.sub("Albus."," Albus ",text)
    text = re.sub("DUMBLEDORE"," Dumbledore ",text)
    text = re.sub("Dumbledores"," Dumbledore ",text)
    text = re.sub("Dumbhedore"," Dumbledore ",text)
    text = re.sub("Dumbkdore"," Dumbledore ",text)
    text = re.sub("Dumbiedore"," Dumbledore ",text)
    text = re.sub("Dumbiedorf"," Dumbledore ",text)
    text = re.sub("Dumbledorf"," Dumbledore ",text)
    text = re.sub("Durnbledore"," Dumbledore ",text)
    text = re.sub("Dumbledoiv"," Dumbledore ",text)
    text = re.sub("Headmasters"," Headmaster ",text)
    # Allgemein
    text = re.sub("GENTLEMEN"," gentlemen ",text)
    text = re.sub("SIR"," sir ",text)
    text = re.sub("LADIES"," ladies ",text)
    text = re.sub("FATHER"," father ",text)
    text = re.sub("FATHERS"," father ",text)
    text = re.sub("HEIR"," heir ",text)
    text = re.sub("'wizard"," wizard ",text)
    text = re.sub("LightningStruck"," Lightning Struck ",text)
    text = re.sub("BROTHERS"," brothers ",text)
    text = re.sub("nowPiertotum"," now Piertotum ",text)
    text = re.sub("schoolSnape"," school Snape ",text)
    text = re.sub("meLISTEN"," me LISTEN ",text)
    text = re.sub("helpI"," help I ",text)
    text = re.sub("Harrylook"," Harry look ",text)
    text = re.sub("serviceI"," service I ",text)
    text = re.sub("Horcruxeshe"," Horcruxe she ",text)
    text = re.sub("hadCrookshanks"," had Crookshanks ",text)
    text = re.sub("Ohrightyeah"," Oh right yeah ",text)
    text = re.sub("AlTeddy*","Albus Teddy",text)
    text = re.sub("DAD"," Dad ",text)
    text = re.sub("HE"," He ",text)
    text = re.sub("Healers"," Healers ",text)
    text = re.sub("him...and"," him and ",text)
    # Angelina Johnson
    text = re.sub("Angelinas'"," Angelina ",text)
    text = re.sub("Angelinas"," Angelina ",text)
    # Argus Filch
    text = re.sub("Filchs'"," Filch ",text)
    text = re.sub("Filchs"," Filch ",text)
    # Aragog
    text = re.sub("Aragogs"," Aragog ",text)
    text = re.sub("Aragog."," Aragog ",text)
    # Armando Dippet
    text = re.sub("Dipper"," Dippet ",text)
    text = re.sub("Dippetto"," Dippet ",text)
    # B
    # Barabas
    text = re.sub("Baraabas"," Barabas ",text)
    # Bathilda
    text = re.sub("Batty"," Bathilda ",text)
    # Bertha
    text = re.sub("Berthas"," Bertha ",text)
    text = re.sub("Berry"," Bertha ",text)
    # Bellatrix Lestrange
    text = re.sub("Lestranges"," Lestranges ",text)
    text = re.sub("[\s,.!?]*Bella[\s\n,.!?]+"," Bellatrix ",text)
    # C
    # Cho Chang
    text = re.sub("Chos"," Cho ",text)
    text = re.sub("[\s,.!?]*CHO[\s,.!?]+"," Cho ",text)
    # Chosen
    text = re.sub("CHOSEN"," Chosen ",text)
    # Cedric Diggory
    text = re.sub("Ced[\s,.!?]+","Cedric",text)
    text = re.sub("CedricI","Cedric I",text)
    text = re.sub("Cedricthat","Cedric that",text)
    text = re.sub("CedricBeaten","Cedric Beaten",text)
    # Celestina Warbeck
    text = re.sub("Celestinas"," Celestina ",text)
    # Cole
    text = re.sub("COLE"," Cole ",text)
    # Colin Creevey
    text = re.sub("Colon"," Colin ",text)
    # Cornelius Fudge
    text = re.sub("CORNELIUS"," Cornelius ",text)
    text = re.sub("Cornelius."," Cornelius ",text)
    text = re.sub("Fudges","Fudge",text)
    # Cormac MacLaggen
    text = re.sub("[\s,.!?]*McLag[\s,.!?]+"," McLaggen ",text)
    # Crabbe
    text = re.sub("Crabbes"," Crabbe ",text)
    # Crouch
    text = re.sub("Barry","Barty",text)
    text = re.sub("Bartys","Barty",text)
    text = re.sub("CROUCH","Crouch",text)
    # D
    # Davies
    text = re.sub("Davey"," Davies ",text)
    # Demelza
    text = re.sub("Demelzas"," Demelza ",text)
    # Dobby
    text = re.sub("DOB[\s\n,.!?]+"," Dobby ",text)
    text = re.sub("DOBBY"," Dobby ",text)
    text = re.sub("ofDobbys"," Dobby ",text)
    # Dolores Umbridge
    text = re.sub("UMBRIDGE"," Umbridge ",text)
    text = re.sub("Umbridges"," Umbridge ",text)
    text = re.sub("Umbndges"," Umbridge ",text)
    text = re.sub("Umbndge"," Umbridge ",text)
    text = re.sub("DoloresT"," Dolores ",text)
    # # Dursleys
    text = re.sub("DURSLEY"," Dursley ",text)
    text = re.sub("Dursleys"," Dursley ",text)
    text = re.sub("Dursleyish"," Dursley ",text)
    text = re.sub("DURSLEYS"," Dursley ",text)
    text = re.sub("DUDLEY"," Dudley ",text)
    text = re.sub("Duddy"," Dudley ",text)
    text = re.sub("Dud[\s\n,.!?]+","Dudley",text)
    text = re.sub("Dudleythat","Dudley that",text)
    text = re.sub("DudleyBut","Dudley but",text)
    text = re.sub("Diddy"," Dudley ",text)
    text = re.sub("Diddykins"," Dudley ",text)
    text = re.sub("Dudders"," Dudley ",text)
    text = re.sub("Dudleys"," Dudley ",text)
    text = re.sub("Budleigh"," Dudley ",text)
    text = re.sub("Popkin"," Dudley ",text)
    text = re.sub("Tuney"," Petunia ",text)
    text = re.sub("PPPetunia"," Petunia ",text)
    text = re.sub("Vernons"," Vernon ",text)
    text = re.sub("Vernoii"," Vernon ",text)
    # F
    # Fawcett
    text = re.sub("Fawcetts"," Fawcett ",text)
    # Fenrir Greyback
    text = re.sub("Fenrit"," Fenrir ",text)
    # Mrs. Fig
    text = re.sub("Figgy"," Fig ",text)
    # Firenze
    text = re.sub("Firenzes"," Firenze ",text)
    # Fleur Delacour
    text = re.sub("Delacours"," Delacour ",text)
    text = re.sub("Fheur"," Fleur ",text)
    # G
    # Gaunt
    text = re.sub("Gaunts"," Gaunt ",text)
    # Gellert Grindelwald
    text = re.sub("Grindelvald"," Grindelwald ",text)
    # Gilderoy
    text = re.sub("GILDEROY"," Gilderoy ",text)
    text = re.sub("Gilderoys"," Gilderoy ",text)
    text = re.sub("Lockharts"," Lockhart ",text)
    # Gornuk
    text = re.sub("Gornuk."," Gornuk ",text)
    # Grawp
    text = re.sub("Grawpy"," Grawp ",text)
    text = re.sub("GRAWPY"," Grawp ",text)
    # Gregorovitch
    text = re.sub("Gregorowitch"," Gregorovitch ",text)
    # Gründer
    text = re.sub("GRYFFINDOR"," Gryffindor ",text)
    text = re.sub("GRYFFINDORS"," Gryffindor ",text)
    text = re.sub("Gryffindors"," Gryffindor ",text)
    text = re.sub("Gryffiindor"," Gryffindor ",text)
    text = re.sub("Gryffmdor"," Gryffindor ",text)
    text = re.sub("Gryfinndor"," Gryffindor ",text)
    text = re.sub("GryffindorRavenclaw"," Gryffindor Ravenclaw ",text)
    text = re.sub("Godric's"," Godric ",text)
    text = re.sub("HUFFLEPUFF"," Hufflepuff ",text)
    text = re.sub("Hufflepuffs"," Hufflepuff ",text)
    text = re.sub("RAVENCLAW"," Ravenclaw ",text)
    text = re.sub("Ravenclaws"," Ravenclaw ",text)
    text = re.sub("SLYTHERIN"," Slytherin ",text)
    text = re.sub("SLYTHERINS"," Slytherin ",text)
    text = re.sub("Slytherins"," Slytherin ",text)
    text = re.sub("Slytherm"," Slytherin ",text)
    # Goyles
    text = re.sub("Goyles"," Goyle ",text)
    # H
    # Harry Potter
    text = re.sub("HarryPotter","Harry Potter",text)
    text = re.sub("POTTER","Potter",text)
    text = re.sub("Potters","Potter",text)
    text = re.sub("PPPotter"," Potter ",text)
    text = re.sub("HARRY"," Harry ",text)
    text = re.sub("Harrys[\s\n,.!?]+"," Harry ",text)
    text = re.sub("Harry..."," Harry ",text)
    text = re.sub("Arry[\s\n,.!?]+","Harry",text)
    text = re.sub("UNDESIRABLE"," Harry ",text)
    text = re.sub("Undesirable"," Harry ",text)
    text = re.sub("'arry","Harry",text)
    text = re.sub("'Harry"," Harry ",text)
    text = re.sub("Harryk[\s\n,.!?]+"," Harry ",text)
    text = re.sub("Parry"," Harry ",text)
    text = re.sub("Barny"," Harry ",text)
    text = re.sub("Garry"," Harry ",text)
    text = re.sub("Bernie"," Harry ",text)
    text = re.sub("Harry-"," Harry ",text)
    text = re.sub("Harvey"," Harry ",text)
    text = re.sub("Harold"," Harry ",text)
    text = re.sub("Jim"," Harry ",text)
    text = re.sub("Ted"," Harry ",text)
    text = re.sub("Howard"," Harry ",text)
    text = re.sub("Harry tter"," Harry Potter ",text)
    text = re.sub("Harry ew"," Harry knew ",text)
    text = re.sub("Harry uld"," Harry could ",text)
    text = re.sub("Harry lt"," Harry felt ",text)
    text = re.sub("HarryZey"," Harry Zey ",text)
    text = re.sub("remember…Harry"," remember Harry ",text)
    text = re.sub("Hogwarts…Harry"," Hogwarts Harry ",text)
    text = re.sub("Harry...and"," Harry and ",text)
    text = re.sub("Harry...I"," Harry I ",text)
    text = re.sub("JAMES"," James ",text)
    text = re.sub("LILY"," Lily ",text)
    text = re.sub("EVANS"," Evans ",text)
    # Hawkshead
    text = re.sub("HAWKSHEAD"," Hawkshead ",text)
    # Hedwig
    text = re.sub("Hedwigs"," Hedwig ",text)
    # Hermione Granger
    text = re.sub("HERMIONE"," Hermione ",text)
    text = re.sub("Hermiones"," Hermione ",text)
    text = re.sub("Herrmone"," Hermione ",text)
    text = re.sub("Herbione"," Hermione ",text)
    text = re.sub("Harmione"," Hermione ",text)
    text = re.sub("Hermoine"," Hermione ",text)
    text = re.sub("Ermynee"," Hermione ",text)
    text = re.sub("Hermy"," Hermione ",text)
    text = re.sub("Grangers"," Granger ",text)
    # Horace Slughorn
    text = re.sub("[\s,.!?]*Sluggy[\s,.!?]*"," Slughorn ",text)
    text = re.sub("Slughorns"," Slughorn ",text)
    text = re.sub("Siughorn"," Slughorn ",text)
    text = re.sub("Slughorh"," Slughorn ",text)
    text = re.sub("Slughotn"," Slughorn ",text)
    text = re.sub("Slugliorn"," Slughorn ",text)
    text = re.sub("Slughoin"," Slughorn ",text)
    text = re.sub("Slughom"," Slughorn ",text)
    # I
    # Igor Karkaroff
    text = re.sub("Karkaroffs"," Karkaroff ",text)
    # K
    # Kingsley Shaklebolt
    text = re.sub("Kmgsley"," Kingsley ",text)
    # L
    # Lavender Brown
    text = re.sub("postLavender"," post Lavender ",text)
    # Lord Voldemort. Tom Riddle
    text = re.sub("VOLDEMORT"," Voldemort ",text)
    text = re.sub("[\s,.!?]*Vol[\s\n,.!?]+"," Voldemort ",text)
    text = re.sub("Vodlemort"," Voldemort ",text)
    text = re.sub("Voldemorts"," Voldemort ",text)
    text = re.sub("VoldemortT"," Voldemort ",text)
    text = re.sub("Voldemord"," Voldemort ",text)
    text = re.sub("Voldy"," Voldemort ",text)
    text = re.sub("RIDDLE"," Voldemort ",text)
    text = re.sub("Riddles"," Voldemort ",text)
    text = re.sub("LORD"," Lord ",text)
    # Ludo Bagman
    text = re.sub("BAGMAN"," Bagman ",text)
    # Luna Lovegood
    text = re.sub("Loony"," Luna ",text)
    text = re.sub("Looooony"," Luna ",text)
    text = re.sub("Lovegoods"," Lovegoods ",text)
    # M
    # MadEye Moody
    text = re.sub("Moodys"," Moody ",text)
    text = re.sub("Mad-Eye"," MadEye ",text)
    # Marauder
    text = re.sub("Padfoot"," Sirius ",text)
    text = re.sub("PADFOOT"," Sirius ",text)
    text = re.sub("SIRIUS"," Sirius ",text)
    text = re.sub("Siriuss"," Sirius ",text)
    text = re.sub("Sirius..."," Sirius ",text)
    text = re.sub("Sirius...and"," Sirius and ",text)
    text = re.sub("Sirius."," Sirius ",text)
    text = re.sub("Blacks"," Black ",text)
    text = re.sub("Snuffles"," Sirius ",text)
    text = re.sub("Wormy"," Peter ",text)
    text = re.sub("Scabbers"," Peter ",text)
    text = re.sub("SCABBERS"," Peter ",text)
    text = re.sub("Moony"," Remus ",text)
    text = re.sub("Lupins"," Lupin ",text)
    text = re.sub("Stag"," James ",text)
    text = re.sub("Prongs"," James ",text)
    text = re.sub("MARAUDER"," Marauder ",text)
    # Master
    text = re.sub("Master..."," Master ",text)
    # Master
    text = re.sub("Masons"," Mason ",text)
    # Malfoy
    text = re.sub("Cissy"," Narcissa ",text)
    text = re.sub("MALFOY"," Malfoy ",text)
    text = re.sub("Malloy"," Malfoy ",text)
    text = re.sub("Maifoy"," Malfoy ",text)
    text = re.sub("Malfoys"," Malfoy ",text)
    text = re.sub("MalfoyIsaDeathEater"," Malfoy Is a Death Eater ",text)
    # Minerva McGonagall
    text = re.sub("MORAN"," Moran ",text)
    # Minerva McGonagall
    text = re.sub("McGonagalls"," McGonagall ",text)
    # Mundungus Fletcher
    text = re.sub("MUNDUNGUS"," Mundungus ",text)
    # Muggle
    text = re.sub("[\s,.!?]+Mugg[\s,.!?]+"," Muggle ",text)
    text = re.sub("Muggles"," Muggle ",text)
    # Myrtle
    text = re.sub("Myrtles"," Myrtle ",text)
    # N
    # Neville Longbottom
    text = re.sub("Longbottoms"," Longbottom ",text)
    text = re.sub("Nevilles"," Neville ",text)
    # Nicholas
    text = re.sub("NICHOLAS"," Nicholas ",text)
    # Nymphadora Tonks
    text = re.sub("[\s,.!?]*Dora[\s,.!?]+"," Nymphadora ",text)
    text = re.sub("Tonkss"," Tonks ",text)
    # O
    # Ollivander
    text = re.sub("Ollivanders"," Ollivander ",text)
    # Oliver Wood
    text = re.sub("OLIVER"," Oliver ",text)
    # Olympe
    text = re.sub("Olympes"," Olympe ",text)
    # P
    # Pansy Parkinson
    text = re.sub("Pansys"," Pansys ",text)
    # Parvati Patil
    text = re.sub("Parvati."," Parvati ",text)
    # Peeves
    text = re.sub("PEEVES"," Peeves ",text)
    text = re.sub("Peevesy"," Peeves ",text)
    text = re.sub("Peevsie"," Peeves ",text)
    # Peverell
    text = re.sub("Peverells"," Peverell ",text)
    # Phineas
    text = re.sub("PHINEAS"," Phineas ",text)
    text = re.sub("Thineas"," Phineas ",text)
    # Piers Polkiss
    text = re.sub("Polkisses"," Polkiss ",text)
    # Porskoff
    text = re.sub("PORSKOFF"," Porskoff ",text)
    # Professor
    text = re.sub("PROFESSOR"," Professor ",text)
    text = re.sub("Professorhead"," Professor head ",text)
    text = re.sub("Professer"," Professor ",text)
    text = re.sub("Professors"," Professor ",text)
    text = re.sub("Professot"," Professor ",text)
    # R
    # Regulus Black
    text = re.sub("[\s,.!?]*Reg[\s\n,.!?]+"," Regulus ",text)
    # Rose Potter
    text = re.sub("Roses"," Rose ",text)
    text = re.sub("Rosie"," Rose ",text)
    # Rowens
    text = re.sub("Rowens"," Rowen ",text)
    # Rubeus Hagrid
    text = re.sub("HAGRID"," Hagrid ",text)
    text = re.sub("HAGGER"," Hagrid ",text)
    text = re.sub("[\s,.!?]*Hag[\s\n,.!?]+","Hagrid",text)
    text = re.sub("Hagrids"," Hagrid ",text)
    text = re.sub("Hagridr"," Hagrid ",text)
    text = re.sub("Hagtid"," Hagrid ",text)
    # S
    # Seamus Finnigan
    text = re.sub("Seamuss"," Seamus ",text)
    # Severus Snape
    text = re.sub("SEVERUS"," Severus ",text)
    text = re.sub("[\s,.!?]*Sev[\s\n,.!?]+"," Severus ",text)
    text = re.sub("Sanpe"," Snape ",text)
    text = re.sub("Snapes"," Snape ",text)
    text = re.sub("Snape."," Snape ",text)
    text = re.sub("Snivdlus"," Snape ",text)
    text = re.sub("Snivellus"," Snape ",text)
    text = re.sub("Snivelly"," Snape ",text)
    text = re.sub("[\s,.!?]*Sn[\s\n,.!?]+"," Snape ",text)
    text = re.sub("[\s,.!?]*Snap[\s\n,.!?]+"," Snape ",text)
    # She
    text = re.sub("SHE"," She ",text)
    # Snatcher
    text = re.sub("Snatcher's"," Snatcher ",text)
    # Stan Shunpike
    text = re.sub("Stanley"," Stan ",text)
    # Sybill Trelawney
    text = re.sub("Trelawneys"," Trelawney ",text)
    text = re.sub("[\s,.!?]*Sybi[\s\n,.!?]+"," Sybill ",text)
    # Squib
    text = re.sub("Squibs"," Squibs ",text)
    # T
    # Troy
    text = re.sub("TROY"," Troy ",text)
    # Todesser
    text = re.sub("ALECTO"," Alecto ",text)
    text = re.sub("ROOKWOOD"," Rookwood ",text)
    text = re.sub("Macnairs"," Macnair ",text)
    text = re.sub("Eaters"," Eater ",text)
    # W
    # Weasleys
    text = re.sub("Ronnie"," Ron ",text)
    text = re.sub("Ronniekins"," Ron ",text)
    text = re.sub("RONALD"," Ron ",text)
    text = re.sub("RON"," Ron ",text)
    text = re.sub("WON"," Ron ",text)
    text = re.sub("Rons"," Ron ",text)
    text = re.sub("Roonil"," Ron ",text)
    text = re.sub("WonWon"," Ron ",text)
    text = re.sub("Georgie"," George ",text)
    text = re.sub("Georges"," George ",text)
    text = re.sub("George."," George ",text)
    text = re.sub("George-ish"," George ",text)
    text = re.sub("GEORGE"," George ",text)
    text = re.sub("Ginevra"," Ginny ",text)
    text = re.sub("Ginny...and"," Ginny and ",text)
    text = re.sub("Ginnyand"," Ginny and ",text)
    text = re.sub("Gmny"," Ginny ",text)
    text = re.sub("Ginny."," Ginny ",text)
    text = re.sub("Perce"," Percy ",text)
    text = re.sub("Percys"," Percy ",text)
    text = re.sub("Perry"," Percy ",text)
    text = re.sub("Charlies"," Charlie ",text)
    text = re.sub("Arthur"," Arthur ",text)
    text = re.sub("Freddie"," Fred ",text)
    text = re.sub("Bill..."," Bill ",text)
    text = re.sub("WEASLEY"," Weasley ",text)
    text = re.sub("WEEZLY"," Weasley ",text)
    text = re.sub("Weatherby"," Weasley ",text)
    text = re.sub("Weasel"," Weasley ",text)
    text = re.sub("Weasleys"," Weasley ",text)
    # Wronski
    text = re.sub("WRONSKI"," Wronski ",text)
    # V
    # Viktor Krum
    text = re.sub("KRUM"," Krum ",text)
    text = re.sub("Vicky"," Viktor ",text)
    # X
    # Xenophilius Lovegood
    text = re.sub("[\s,.!?]*Xeno[\s\n,.!?]+"," Xenophilius ",text)
    # Z
    # Zentauren
    text = re.sub("BANE"," Bane ",text)
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
        cleantext = rawtext.replace('\xad','')
        unifiedtext = cleanData(cleantext)
        # Bereinigten Text in Datei schreiben
        with open(os.path.join('Data','REFINED',str(i)+'.txt'),'w',encoding='utf-8') as f:
            f.write(unifiedtext)

def createMasterText():
    # Refined Dateidirectory auslesen. Iterieren über Dateien
    files = os.listdir('Data\REFINED')
    text = ''
    for i in range(0,len(files)):
        # Dateien auslesen
        with open(os.path.join('Data','REFINED',files[i]),'r',encoding='utf-8') as f:
            content = f.read()
        text += content
    with open(os.path.join('Data','REFINED','master.txt'),'w',encoding='utf-8') as f:
        f.write(text)
