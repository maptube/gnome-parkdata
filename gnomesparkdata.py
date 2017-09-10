#!/usr/bin/env python3

import os
import sys
import csv


def main():
    infilename = "C:\\Users\\richard\\Desktop\\Gnomes\\SIGCHI\\gnome-data\\conversations.csv"
    print("loading: ", infilename)

    creatureNames = [ 'Parker', 'Wombat', 'Loki', 'Gnomeo', 'Jetpack Gnomey', 'Super Gnome', 'Yusuf',
                      'Denchu', 'Zack', 'Khadija',
                      'Rosie', 'Beehigh',
                      'Moonlight', 'Goku', 'Shadow Blade' ]

    #chatbot text following the user's yes or no after memory prompt
    #TODO: could also track "username YES|NO"
    memoryTextYes = "Perfect! What would you like to tell me?"
    memoryTextNo = "No problem " #plus name

    #cID, INTERLOCUTOR, TEXT, LAT, LON
    #108, Duncan, hello, 51.54592, -0.01443
    #108, Denchu, "Hi! I'm Otter 1, and I'm a Memory Gnome", 51.54592, -0.01443

    namecount = {}
    memoryyescount = {}
    memorynocount = {}
    wordcount = {}
    with open(infilename, 'rt') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            #print(', '.join(row))
            print (row)
            cid=row[0]
            name=row[1]
            text=row[2]
            #set a flag to say whether the line is spoken by the creature or the visitor
            isGnomeText = name in creatureNames

            #count unique names - gnomes and users
            if name in namecount:
                namecount[name]=namecount[name]+1
            else:
                namecount[name]=1
            #count memories - either yes for memory left, or no for declined to leave one
            if text==memoryTextYes:
                if name in memoryyescount:
                    memoryyescount[name]=memoryyescount[name]+1
                else:
                    memoryyescount[name]=1
            if text.startswith(memoryTextNo):
                if name in memorynocount:
                    memorynocount[name]=memorynocount[name]+1
                else:
                    memorynocount[name]=1
            #word counts - but only from the visitors
            if not isGnomeText:
                words = text.split()
                for word in words:
                    word = word.lower()
                    word=word.replace(',','')
                    word=word.replace('.','')
                    word=word.replace('!','')
                    if word in wordcount:
                        wordcount[word]=wordcount[word]+1
                    else:
                        wordcount[word]=1


    ###
    #print("namecount")
    for key, value in namecount.items():
        memoryYes=0
        memoryNo=0
        if key in memoryyescount:
            memoryYes=memoryyescount[key]
        if key in memorynocount:
            memoryNo=memorynocount[key]
        print(key, ",", value, ",", memoryYes, ",", memoryNo)

    #word counts
    print("word counts")
    for key, value in wordcount.items():
        print(key, ",", value)


###############################################################################
if __name__ == "__main__":
    main()