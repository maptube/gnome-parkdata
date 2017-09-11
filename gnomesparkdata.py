#!/usr/bin/env python3

import os
import sys
import csv


def main():
    #infilename = "C:\\Users\\richard\\Desktop\\Gnomes\\SIGCHI\\gnome-data\\conversations.csv"
    infilename = "C:\\Users\\richard\\Desktop\\SIGCHI\\gnomes-data\\20170911_conversations\\conversations_sep.csv"
    print("loading: ", infilename)

    creatureNames = [ 'Parker', 'Wombat', 'Loki', 'Gnomeo', 'Jetpack Gnomey', 'Super Gnome', 'Yusuf',
                      'Denchu', 'Zack', 'Khadija',
                      'Rosie', 'Beehigh',
                      'Moonlight', 'Goku', 'Shadow Blade' ]

    #chatbot text following the user's yes or no after memory prompt
    #TODO: could also track "username YES|NO"
    memoryTextYes = [
        "Perfect! What would you like to tell me?",
        "Great! What would you like to tell me?",
        "Great! What's your memory about?" ]
    memoryTextNo = "No problem " #plus name

    #chatbot text when user meets a second gnome
    otherGnomeText = [
        "I see you've already spoken to ", #plus creature name
        "You just spoke to ", #plus creature name
        "I see you've just spoken to " #plus creature name
    ]

    #nextCreatureText = "You can find my buddy "

    #cID, INTERLOCUTOR, TEXT, LAT, LON
    #108, Duncan, hello, 51.54592, -0.01443
    #108, Denchu, "Hi! I'm Otter 1, and I'm a Memory Gnome", 51.54592, -0.01443

    namecount = {}
    memoryyescount = {}
    memorynocount = {}
    othergnomecount = {}
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
            #count memories - either yes for memory was left, or no for declined to leave one
            if text in memoryTextYes:
                if name in memoryyescount:
                    memoryyescount[name]=memoryyescount[name]+1
                else:
                    memoryyescount[name]=1
            if text.startswith(memoryTextNo):
                if name in memorynocount:
                    memorynocount[name]=memorynocount[name]+1
                else:
                    memorynocount[name]=1
            #repeat counts when it detects you have visited another gnome before
            for ogtext in otherGnomeText:
                if text.startswith(ogtext):
                    if name in othergnomecount:
                        othergnomecount[name]=othergnomecount[name]+1
                    else:
                        othergnomecount[name]=1
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
    print("name,count,memyes,memno,othergnomes")
    for key, value in namecount.items():
        memoryYes=0
        memoryNo=0
        ogcount=0
        if key in memoryyescount:
            memoryYes=memoryyescount[key]
        if key in memorynocount:
            memoryNo=memorynocount[key]
        if key in othergnomecount:
            ogcount=othergnomecount[key]
        print(key, ",", value, ",", memoryYes, ",", memoryNo, ",", ogcount)

    #word counts
    print("")
    print("word counts")
    for key, value in wordcount.items():
        print(key, ",", value)


###############################################################################
if __name__ == "__main__":
    main()