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
    text = re.sub("[\s,.!?]ALBUS[\s,.!?]"," Albus ",text)
    text = re.sub("[\s,.!?]Percival[\s,.!?]"," Albus ",text)
    text = re.sub("[\s,.!?]Al[\s,.!?]"," Albus ",text)
    text = re.sub("[\s,.!?]Ablus[\s,.!?]"," Albus ",text)
    text = re.sub("[\s,.!?]Albus.[\s,.!?]"," Albus ",text)
    text = re.sub("[\s,.!?]DUMBLEDORE[\s,.!?]"," Dumbledore ",text)
    text = re.sub("[\s,.!?]Dumbledores[\s,.!?]"," Dumbledore ",text)
    text = re.sub("[\s,.!?]Dumbhedore[\s,.!?]"," Dumbledore ",text)
    text = re.sub("[\s,.!?]Dumbkdore[\s,.!?]"," Dumbledore ",text)
    text = re.sub("[\s,.!?]Dumbiedore[\s,.!?]"," Dumbledore ",text)
    text = re.sub("[\s,.!?]Dumbiedorf[\s,.!?]"," Dumbledore ",text)
    text = re.sub("[\s,.!?]Dumbledoiv[\s,.!?]"," Dumbledore ",text)
    # Allgemein
    text = re.sub("[\s,.!?]GENTLEMEN[\s,.!?]"," gentlemen ",text)
    text = re.sub("[\s,.!?]SIR[\s,.!?]"," sir ",text)
    text = re.sub("[\s,.!?]LADIES[\s,.!?]"," ladies ",text)
    text = re.sub("[\s,.!?]FATHER[\s,.!?]"," father ",text)
    text = re.sub("[\s,.!?]FATHERS[\s,.!?]"," father ",text)
    text = re.sub("[\s,.!?]HEIR[\s,.!?]"," heir ",text)
    text = re.sub("[\s,.!?]'wizard[\s,.!?]"," wizard ",text)
    text = re.sub("[\s,.!?]LightningStruck[\s,.!?]"," Lightning Struck ",text)
    text = re.sub("[\s,.!?]BROTHERS[\s,.!?]"," brothers ",text)
    text = re.sub("[\s,.!?]nowPiertotum[\s,.!?]"," now Piertotum ",text)
    text = re.sub("[\s,.!?]schoolSnape[\s,.!?]"," school Snape ",text)
    text = re.sub("[\s,.!?]meLISTEN[\s,.!?]"," me LISTEN ",text)
    text = re.sub("[\s,.!?]helpI[\s,.!?]"," help I ",text)
    text = re.sub("[\s,.!?]Harrylook[\s,.!?]"," Harry look ",text)
    text = re.sub("[\s,.!?]serviceI[\s,.!?]"," service I ",text)
    text = re.sub("[\s,.!?]Horcruxeshe[\s,.!?]"," Horcruxe she ",text)
    text = re.sub("[\s,.!?]hadCrookshanks[\s,.!?]"," had Crookshanks ",text)
    text = re.sub("[\s,.!?]Ohrightyeah[\s,.!?]"," Oh right yeah ",text)
    text = re.sub("[\s,.!?]AlTeddy[\s,.!?]"," Albus Teddy ",text)
    text = re.sub("[\s,.!?]DAD[\s,.!?]"," Dad ",text)
    # Angelina Johnson
    text = re.sub("[\s,.!?]Angelinas'[\s,.!?]"," Angelina ",text)
    # Argus Filch
    text = re.sub("[\s,.!?]Filchs'[\s,.!?]"," Filch ",text)
    # Aragog
    text = re.sub("[\s,.!?]Aragogs[\s,.!?]"," Aragog ",text)
    text = re.sub("[\s,.!?]Aragog.[\s,.!?]"," Aragog ",text)
    # B
    # Barabas
    text = re.sub("[\s,.!?]Baraabas[\s,.!?]"," Barabas ",text)
    # Bathilda
    text = re.sub("[\s,.!?]Batty[\s,.!?]"," Bathilda ",text)
    # Bertha
    text = re.sub("[\s,.!?]Berthas[\s,.!?]"," Bertha ",text)
    text = re.sub("[\s,.!?]Berry[\s,.!?]"," Bertha ",text)
    # Bellatrix Lestrange
    text = re.sub("[\s,.!?]Lestranges[\s,.!?]"," Lestranges ",text)
    text = re.sub("[\s,.!?]Bella[\s,.!?]"," Bellatrix ",text)
    # C
    # Cho Chang
    text = re.sub("[\s,.!?]Chos[\s,.!?]"," Cho ",text)
    text = re.sub("[\s,.!?]CHO[\s,.!?]"," Cho ",text)
    # Chosen
    text = re.sub("[\s,.!?]CHOSEN[\s,.!?]"," Chosen ",text)
    # Cedric Diggory
    text = re.sub("[\s,.!?]Ced[\s,.!?]"," Cedric ",text)
    # Celestina Warbeck
    text = re.sub("[\s,.!?]Celestinas[\s,.!?]"," Celestina ",text)
    # Cole
    text = re.sub("[\s,.!?]COLE[\s,.!?]"," Cole ",text)
    # Colin Creevey
    text = re.sub("[\s,.!?]Colon[\s,.!?]"," Colin ",text)
    # Cornelius Fudge
    text = re.sub("[\s,.!?]CORNELIUS[\s,.!?]"," Cornelius ",text)
    # Cormac MacLaggen
    text = re.sub("[\s,.!?]McLag[\s,.!?]"," McLaggen ",text)
    # Crabbe
    text = re.sub("[\s,.!?]Crabbes[\s,.!?]"," Crabbe ",text)
    # D
    # Demelza
    text = re.sub("[\s,.!?]Demelzas[\s,.!?]"," Demelza ",text)
    # Dobby
    text = re.sub("[\s,.!?]DOB[\s,.!?]"," Dobby ",text)
    text = re.sub("[\s,.!?]DOBBY[\s,.!?]"," Dobby ",text)
    text = re.sub("[\s,.!?]ofDobbys[\s,.!?]"," Dobby ",text)
    # Dolores Umbridge
    text = re.sub("[\s,.!?]UMBRIDGE[\s,.!?]"," Umbridge ",text)
    text = re.sub("[\s,.!?]Umbridges[\s,.!?]"," Umbridge ",text)
    text = re.sub("[\s,.!?]Umbndges[\s,.!?]"," Umbridge ",text)
    text = re.sub("[\s,.!?]DoloresT[\s,.!?]"," Dolores ",text)
    # Dursleys
    text = re.sub("[\s,.!?]DURSLEY[\s,.!?]"," Dursley ",text)
    text = re.sub("[\s,.!?]Dursleys[\s,.!?]|"," Dursley ",text)
    text = re.sub("[\s,.!?]Dursleyish[\s,.!?]|"," Dursley ",text)
    text = re.sub("[\s,.!?]DURSLEYS[\s,.!?]"," Dursley ",text)
    text = re.sub("[\s,.!?]Duddy[\s,.!?]"," Dudley ",text)
    text = re.sub("[\s,.!?]Dud[\s,.!?]"," Dudley ",text)
    text = re.sub("[\s,.!?]Diddy[\s,.!?]"," Dudley ",text)
    text = re.sub("[\s,.!?]Diddykins[\s,.!?]"," Dudley ",text)
    text = re.sub("[\s,.!?]Dudders[\s,.!?]"," Dudley ",text)
    text = re.sub("[\s,.!?]Dudleys[\s,.!?]"," Dudley ",text)
    text = re.sub("[\s,.!?]Budleigh[\s,.!?]"," Dudley ",text)
    text = re.sub("[\s,.!?]Popkin[\s,.!?]"," Dudley ",text)
    text = re.sub("[\s,.!?]DUDLEY[\s,.!?]"," Dudley ",text)
    text = re.sub("[\s,.!?]Tuney[\s,.!?]"," Petunia ",text)
    text = re.sub("[\s,.!?]PPPetunia[\s,.!?]"," Petunia ",text)
    text = re.sub("[\s,.!?]Vernons[\s,.!?]"," Vernon ",text)
    text = re.sub("[\s,.!?]Vernoii[\s,.!?]"," Vernon ",text)
    # F
    # Fawcett
    text = re.sub("[\s,.!?]Fawcetts[\s,.!?]"," Fawcett ",text)
    # Fenrir Greyback
    text = re.sub("[\s,.!?]Fenrit[\s,.!?]"," Fenrir ",text)
    # Mrs. Fig
    text = re.sub("[\s,.!?]Figgy[\s,.!?]"," Fig ",text)
    # Firenze
    text = re.sub("[\s,.!?]Firenzes[\s,.!?]"," Firenze ",text)
    # Fleur Delacour
    text = re.sub("[\s,.!?]Delacours[\s,.!?]"," Delacour ",text)
    text = re.sub("[\s,.!?]Fheur[\s,.!?]"," Fleur ",text)
    # G
    # Gaunt
    text = re.sub("[\s,.!?]Gaunts[\s,.!?]"," Gaunt ",text)
    # Gellert Grindelwald
    text = re.sub("[\s,.!?]Grindelvald[\s,.!?]"," Grindelwald ",text)
    # Gilderoy
    text = re.sub("[\s,.!?]GILDEROY[\s,.!?]"," Gilderoy ",text)
    text = re.sub("[\s,.!?]Gilderoys[\s,.!?]"," Gilderoy ",text)
    # Gornuk
    text = re.sub("[\s,.!?]Gornuk.[\s,.!?]"," Gornuk ",text)
    # Grawp
    text = re.sub("[\s,.!?]Grawpy[\s,.!?]"," Grawp ",text)
    text = re.sub("[\s,.!?]GRAWPY[\s,.!?]"," Grawp ",text)
    # Gregorovitch
    text = re.sub("[\s,.!?]Gregorowitch[\s,.!?]"," Gregorovitch ",text)
    # Gründer
    text = re.sub("[\s,.!?]GRYFFINDOR[\s,.!?]"," Gryffindor ",text)
    text = re.sub("[\s,.!?]GRYFFINDORS[\s,.!?]"," Gryffindor ",text)
    text = re.sub("[\s,.!?]Gryffindors[\s,.!?]"," Gryffindor ",text)
    text = re.sub("[\s,.!?]Gryffiindor[\s,.!?]"," Gryffindor ",text)
    text = re.sub("[\s,.!?]Gryffmdor[\s,.!?]"," Gryffindor ",text)
    text = re.sub("[\s,.!?]Gryfinndor[\s,.!?]"," Gryffindor ",text)
    text = re.sub("[\s,.!?]GryffindorRavenclaw[\s,.!?]"," Gryffindor Ravenclaw ",text)
    text = re.sub("[\s,.!?]Godric's[\s,.!?]"," Godric ",text)
    text = re.sub("[\s,.!?]HUFFLEPUFF[\s,.!?]"," Hufflepuff ",text)
    text = re.sub("[\s,.!?]RAVENCLAW[\s,.!?]"," Ravenclaw ",text)
    text = re.sub("[\s,.!?]SLYTHERIN[\s,.!?]"," Slytherin ",text)
    text = re.sub("[\s,.!?]SLYTHERINS[\s,.!?]"," Slytherin ",text)
    # Goyles
    text = re.sub("[\s,.!?]Goyles[\s,.!?]"," Goyle ",text)
    # H
    # Harry Potter
    text = re.sub("[\s,.!?]POTTER[\s,.!?]"," Potter ",text)
    text = re.sub("[\s,.!?]Potters[\s,.!?]"," Potter ",text)
    text = re.sub("[\s,.!?]PPPotter[\s,.!?]"," Potter ",text)
    text = re.sub("[\s,.!?]HARRY[\s,.!?]"," Harry ",text)
    text = re.sub("[\s,.!?]Harrys[\s,.!?]"," Harry ",text)
    text = re.sub("[\s,.!?]Arry[\s,.!?]"," Harry ",text)
    text = re.sub("[\s,.!?]UNDESIRABLE[\s,.!?]"," Harry ",text)
    text = re.sub("[\s,.!?]Undesirable[\s,.!?]"," Harry ",text)
    text = re.sub("[\s,.!?]'arry[\s,.!?]"," Harry ",text)
    text = re.sub("[\s,.!?]'Harry[\s,.!?]"," Harry ",text)
    text = re.sub("[\s,.!?]Harryk[\s,.!?]"," Harry ",text)
    text = re.sub("[\s,.!?]Harrys[\s,.!?]"," Harry ",text)
    text = re.sub("[\s,.!?]Parry[\s,.!?]"," Harry ",text)
    text = re.sub("[\s,.!?]Barny[\s,.!?]"," Harry ",text)
    text = re.sub("[\s,.!?]Garry[\s,.!?]"," Harry ",text)
    text = re.sub("[\s,.!?]Bernie[\s,.!?]"," Harry ",text)
    text = re.sub("[\s,.!?]Harry-[\s,.!?]"," Harry ",text)
    text = re.sub("[\s,.!?]remember…Harry[\s,.!?]"," remember Harry ",text)
    text = re.sub("[\s,.!?]Hogwarts…Harry[\s,.!?]"," Hogwarts Harry ",text)
    text = re.sub("[\s,.!?]Harry...and[\s,.!?]"," Harry and ",text)
    text = re.sub("[\s,.!?]Harry...I[\s,.!?]"," Harry I ",text)
    text = re.sub("[\s,.!?]JAMES[\s,.!?]"," James ",text)
    text = re.sub("[\s,.!?]LILY[\s,.!?]"," Lily ",text)
    text = re.sub("[\s,.!?]EVANS[\s,.!?]"," Evans ",text)
    # Hawkshead
    text = re.sub("[\s,.!?]HAWKSHEAD[\s,.!?]"," Hawkshead ",text)
    # He
    text = re.sub("[\s,.!?]HE[\s,.!?]"," He ",text)
    # Hedwig
    text = re.sub("[\s,.!?]Hedwigs[\s,.!?]"," Hedwig ",text)
    # Hermione Granger
    text = re.sub("[\s,.!?]HERMIONE[\s,.!?]"," Hermione ",text)
    text = re.sub("[\s,.!?]Herrmone[\s,.!?]"," Hermione ",text)
    text = re.sub("[\s,.!?]Harmione[\s,.!?]"," Hermione ",text)
    text = re.sub("[\s,.!?]Ermynee[\s,.!?]"," Hermione ",text)
    # Hepzibah
    text = re.sub("[\s,.!?]Hepzibah[\s,.!?]"," Hermione ",text)
    # Horace Slughorn
    text = re.sub("[\s,.!?]Sluggy[\s,.!?]"," Slughorn ",text)
    text = re.sub("[\s,.!?]Slughorns[\s,.!?]"," Slughorn ",text)
    text = re.sub("[\s,.!?]Siughorn[\s,.!?]"," Slughorn ",text)
    text = re.sub("[\s,.!?]Slughorh[\s,.!?]"," Slughorn ",text)
    text = re.sub("[\s,.!?]Slughotn[\s,.!?]"," Slughorn ",text)
    text = re.sub("[\s,.!?]Slugliorn[\s,.!?]"," Slughorn ",text)
    text = re.sub("[\s,.!?]Slughoin[\s,.!?]"," Slughorn ",text)
    text = re.sub("[\s,.!?]Slughom[\s,.!?]"," Slughorn ",text)
    # I
    # Igor Karkaroff
    text = re.sub("[\s,.!?]Karkaroffs[\s,.!?]"," Karkaroff ",text)
    # K
    # Kingsley Shaklebolt
    text = re.sub("[\s,.!?]Kmgsley[\s,.!?]"," Kingsley ",text)
    # L
    # Lavender Brown
    text = re.sub("[\s,.!?]postLavender[\s,.!?]"," post Lavender ",text)
    # Lord Voldemort. Tom Riddle
    text = re.sub("[\s,.!?]VOLDEMORT[\s,.!?]"," Voldemort ",text)
    text = re.sub("[\s,.!?]Vol[\s,.!?]"," Voldemort ",text)
    text = re.sub("[\s,.!?]Vodlemort[\s,.!?]"," Voldemort ",text)
    text = re.sub("[\s,.!?]Voldemorts[\s,.!?]"," Voldemort ",text)
    text = re.sub("[\s,.!?]VoldemortT[\s,.!?]"," Voldemort ",text)
    text = re.sub("[\s,.!?]Voldemord[\s,.!?]"," Voldemort ",text)
    text = re.sub("[\s,.!?]Voldy[\s,.!?]"," Voldemort ",text)
    text = re.sub("[\s,.!?]TOM[\s,.!?]"," Voldemort ",text)
    text = re.sub("[\s,.!?]RIDDLE[\s,.!?]"," Voldemort ",text)
    text = re.sub("[\s,.!?]Riddles[\s,.!?]"," Voldemort ",text)
    text = re.sub("[\s,.!?]LORD[\s,.!?]"," Lord ",text)
    # Ludo Bagman
    text = re.sub("[\s,.!?]BAGMAN[\s,.!?]"," Bagman ",text)
    # Luna Lovegood
    text = re.sub("[\s,.!?]Loony[\s,.!?]"," Luna ",text)
    text = re.sub("[\s,.!?]Looooony[\s,.!?]"," Luna ",text)
    text = re.sub("[\s,.!?]Lovegood[\s,.!?]"," Lovegoods ",text)
    # M
    # MadEye Moody
    text = re.sub("[\s,.!?]Moodys[\s,.!?]"," Moody ",text)
    text = re.sub("[\s,.!?]Mad-Eye[\s,.!?]"," MadEye ",text)
    # Marauder
    text = re.sub("[\s,.!?]Padfoot[\s,.!?]"," Sirius ",text)
    text = re.sub("[\s,.!?]PADFOOT[\s,.!?]"," Sirius ",text)
    text = re.sub("[\s,.!?]SIRIUS[\s,.!?]"," Sirius ",text)
    text = re.sub("[\s,.!?]Siriuss[\s,.!?]"," Sirius ",text)
    text = re.sub("[\s,.!?]Sirius...[\s,.!?]"," Sirius ",text)
    text = re.sub("[\s,.!?]Sirius...and[\s,.!?]"," Sirius and ",text)
    text = re.sub("[\s,.!?]Blacks[\s,.!?]"," Black ",text)
    text = re.sub("[\s,.!?]Snuffles[\s,.!?]"," Sirius ",text)
    text = re.sub("[\s,.!?]Wormy[\s,.!?]"," Peter ",text)
    text = re.sub("[\s,.!?]Scabbers[\s,.!?]"," Peter ",text)
    text = re.sub("[\s,.!?]SCABBERS[\s,.!?]"," Peter ",text)
    text = re.sub("[\s,.!?]Moony[\s,.!?]"," Remus ",text)
    text = re.sub("[\s,.!?]Lupins[\s,.!?]"," Lupin ",text)
    text = re.sub("[\s,.!?]Stag[\s,.!?]"," James ",text)
    text = re.sub("[\s,.!?]Prongs[\s,.!?]"," James ",text)
    text = re.sub("[\s,.!?]MARAUDER[\s,.!?]"," Marauder ",text)
    # Master
    text = re.sub("[\s,.!?]Master...[\s,.!?]"," Master ",text)
    # Malfoy
    text = re.sub("[\s,.!?]Cissy[\s,.!?]"," Narcissa ",text)
    text = re.sub("[\s,.!?]MALFOY[\s,.!?]"," Malfoy ",text)
    text = re.sub("[\s,.!?]Malloy[\s,.!?]"," Malfoy ",text)
    text = re.sub("[\s,.!?]Maifoy[\s,.!?]"," Malfoy ",text)
    text = re.sub("[\s,.!?]MalfoyIsaDeathEater[\s,.!?]"," Malfoy Is a Death Eater ",text)
    # Minerva McGonagall
    text = re.sub("[\s,.!?]MORAN[\s,.!?]"," Moran ",text)
    # Minerva McGonagall
    text = re.sub("[\s,.!?]McGonagalls[\s,.!?]"," McGonagall ",text)
    # Mundungus Fletcher
    text = re.sub("[\s,.!?]MUNDUNGUS[\s,.!?]"," Mundungus ",text)
    # Myrtle
    text = re.sub("[\s,.!?]Myrtles[\s,.!?]"," Myrtle ",text)
    # N
    # Neville Longbottom
    text = re.sub("[\s,.!?]Longbottoms[\s,.!?]"," Longbottom ",text)
    text = re.sub("[\s,.!?]Nevilles[\s,.!?]"," Neville ",text)
    # Nicholas
    text = re.sub("[\s,.!?]NICHOLAS[\s,.!?]"," Nicholas ",text)
    # Nymphadora Tonks
    text = re.sub("[\s,.!?]Dora[\s,.!?]"," Nymphadora ",text)
    text = re.sub("[\s,.!?]Tonkss[\s,.!?]"," Tonks ",text)
    # O
    # Oliver Wood
    text = re.sub("[\s,.!?]OLIVER[\s,.!?]"," Oliver ",text)
    # Olympe
    text = re.sub("[\s,.!?]Olympes[\s,.!?]"," Olympe ",text)
    # P
    # Pansy Parkinson
    text = re.sub("[\s,.!?]Pansys[\s,.!?]"," Pansys ",text)
    # Peeves
    text = re.sub("[\s,.!?]PEEVES[\s,.!?]"," Peeves ",text)
    text = re.sub("[\s,.!?]Peevesy[\s,.!?]"," Peeves ",text)
    text = re.sub("[\s,.!?]Peevsie[\s,.!?]"," Peeves ",text)
    # Peverell
    text = re.sub("[\s,.!?]Peverells[\s,.!?]"," Peverell ",text)
    # Phineas
    text = re.sub("[\s,.!?]PHINEAS[\s,.!?]"," Phineas ",text)
    text = re.sub("[\s,.!?]Thineas[\s,.!?]"," Phineas ",text)
    # Piers Polkiss
    text = re.sub("[\s,.!?]Polkisses[\s,.!?]"," Polkiss ",text)
    # Porskoff
    text = re.sub("[\s,.!?]PORSKOFF[\s,.!?]"," Porskoff ",text)
    # Professor
    text = re.sub("[\s,.!?]PROFESSOR[\s,.!?]"," Professor ",text)
    text = re.sub("[\s,.!?]Professorhead[\s,.!?]"," Professor head ",text)
    # R
    # Regulus Black
    text = re.sub("[\s,.!?]Reg[\s,.!?]"," Regulus ",text)
    # Rose Potter
    text = re.sub("[\s,.!?]Roses[\s,.!?]"," Rose ",text)
    text = re.sub("[\s,.!?]Rosie[\s,.!?]"," Rose ",text)
    # Rowens
    text = re.sub("[\s,.!?]Rowens[\s,.!?]"," Rowen ",text)
    # Rubeus Hagrid
    text = re.sub("[\s,.!?]HAGRID[\s,.!?]"," Hagrid ",text)
    text = re.sub("[\s,.!?]HAGGER[\s,.!?]"," Hagrid ",text)
    text = re.sub("[\s,.!?]Hag[\s,.!?]"," Hagrid ",text)
    text = re.sub("[\s,.!?]Hagrids[\s,.!?]"," Hagrid ",text)
    text = re.sub("[\s,.!?]Hagridr[\s,.!?]"," Hagrid ",text)
    # S
    # Seamus Finnigan
    text = re.sub("[\s,.!?]Seamuss[\s,.!?]"," Seamus ",text)
    # Severus Snape
    text = re.sub("[\s,.!?]SEVERUS[\s,.!?]"," Severus ",text)
    text = re.sub("[\s,.!?]Sev[\s,.!?]"," Severus ",text)
    text = re.sub("[\s,.!?]Sanpe[\s,.!?]"," Snape ",text)
    text = re.sub("[\s,.!?]Snapes[\s,.!?]"," Snape ",text)
    text = re.sub("[\s,.!?]Snivdlus[\s,.!?]"," Snape ",text)
    text = re.sub("[\s,.!?]Snivellus[\s,.!?]"," Snape ",text)
    text = re.sub("[\s,.!?]Snivelly[\s,.!?]"," Snape ",text)
    text = re.sub("[\s,.!?]Sn[\s,.!?]"," Snape ",text)
    # She
    text = re.sub("[\s,.!?]SHE[\s,.!?]"," She ",text)
    # Snatcher
    text = re.sub("[\s,.!?]Snatcher[\s,.!?]"," Snatcher's ",text)
    # Stan Shunpike
    text = re.sub("[\s,.!?]Stanley[\s,.!?]"," Stan ",text)
    # Sybill Trelawney
    text = re.sub("[\s,.!?]Trelawneys[\s,.!?]"," Trelawney ",text)
    text = re.sub("[\s,.!?]Sybi[\s,.!?]"," Sybill ",text)
    # T
    # Troy
    text = re.sub("[\s,.!?]TROY[\s,.!?]"," Troy ",text)
    # Todesser
    text = re.sub("[\s,.!?]ALECTO[\s,.!?]"," Alecto ",text)
    text = re.sub("[\s,.!?]ROOKWOOD[\s,.!?]"," Rookwood ",text)
    text = re.sub("[\s,.!?]Macnairs[\s,.!?]"," Macnair ",text)
    # W
    # Weasleys
    text = re.sub("[\s,.!?]Ronnie[\s,.!?]"," Ron ",text)
    text = re.sub("[\s,.!?]Ronniekins[\s,.!?]"," Ron ",text)
    text = re.sub("[\s,.!?]RONALD[\s,.!?]"," Ron ",text)
    text = re.sub("[\s,.!?]RON[\s,.!?]"," Ron ",text)
    text = re.sub("[\s,.!?]WON[\s,.!?]"," Ron ",text)
    text = re.sub("[\s,.!?]Rons[\s,.!?]"," Ron ",text)
    text = re.sub("[\s,.!?]Roonil[\s,.!?]"," Ron ",text)
    text = re.sub("[\s,.!?]WonWon[\s,.!?]"," Ron ",text)
    text = re.sub("[\s,.!?]Georgie[\s,.!?]"," George ",text)
    text = re.sub("[\s,.!?]Georges[\s,.!?]"," George ",text)
    text = re.sub("[\s,.!?]George.[\s,.!?]"," George ",text)
    text = re.sub("[\s,.!?]George-ish[\s,.!?]"," George ",text)
    text = re.sub("[\s,.!?]GEORGE[\s,.!?]"," George ",text)
    text = re.sub("[\s,.!?]Ginevra[\s,.!?]"," Ginny ",text)
    text = re.sub("[\s,.!?]Ginny...and[\s,.!?]"," Ginny and ",text)
    text = re.sub("[\s,.!?]Ginnyand[\s,.!?]"," Ginny and ",text)
    text = re.sub("[\s,.!?]Gmny[\s,.!?]"," Ginny ",text)
    text = re.sub("[\s,.!?]Ginny.[\s,.!?]"," Ginny ",text)
    text = re.sub("[\s,.!?]Perce[\s,.!?]"," Percy ",text)
    text = re.sub("[\s,.!?]Percys[\s,.!?]"," Percy ",text)
    text = re.sub("[\s,.!?]Charlies[\s,.!?]"," Charlie ",text)
    text = re.sub("[\s,.!?]Arthur[\s,.!?]"," Arthur ",text)
    text = re.sub("[\s,.!?]Freddie[\s,.!?]"," Fred ",text)
    text = re.sub("[\s,.!?]WEASLEY[\s,.!?]"," Weasley ",text)
    text = re.sub("[\s,.!?]WEEZLY[\s,.!?]"," Weasley ",text)
    text = re.sub("[\s,.!?]Weatherby[\s,.!?]"," Weasley ",text)
    text = re.sub("[\s,.!?]Weasel[\s,.!?]"," Weasley ",text)
    # Wronski
    text = re.sub("[\s,.!?]WRONSKI[\s,.!?]"," Wronski ",text)
    # V
    # Viktor Krum
    text = re.sub("[\s,.!?]KRUM[\s,.!?]"," Krum ",text)
    # X
    # Xenophilius Lovegood
    text = re.sub("[\s,.!?]Xeno[\s,.!?]"," Xenophilius ",text)
    # Z
    # Zentauren
    text = re.sub("[\s,.!?]BANE[\s,.!?]"," Bane ",text)
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
    for i in range(1,len(files)):
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
