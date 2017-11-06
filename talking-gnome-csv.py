#!/usr/bin/env python3

import os
import sys
import csv
import time
import random

#Like talkinggnome.py on the Raspberry Pi, except it uses canned data from a csv file instead

#list of conversations
conversations = []

class ConversationLine:
    """One line of the conversation"""
    def __init__(self, speaker, text):
        self.speaker = speaker
        self.text = text;


############################################################################################################

def speak(text):
    """
    Speech synthesis, basically an os command with FLite
    :param text:
    :return:
    """
    text = text.replace('"','')
    print('flite -t "'+text+'"')
    #os.whatever...

############################################################################################################

def speakConversation(conversation):
    for line in conversation:
        speak(line.speaker+', '+line.text)

############################################################################################################

def loadData(infile):
    """
    Load conversations from csv file into conversations structure (list of ConversationLine list)
    Precondition: infile conversation list must be grouped by cid number
    :param infile:
    :return:
    """
    with open(infile, 'rt') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader) #skip header
        lastcid = -1
        conversation = [] #ordered list of ConversationLine objects
        for row in reader:
            cid = row[0]
            name = row[1]
            text = row[2]
            if cid!=lastcid and len(conversation)>0:
                #different conversation id and not the first
                conversations.append(conversation)
                conversation=[] #start a new conversation
            lastcid=cid
            conversation.append(ConversationLine(name,text))
        #don't forget to push the last conversation in the file...
        conversations.append(conversation)

######################################################################################################



def main():
    #infilename = "C:\\Users\\richard\\Desktop\\Gnomes\\SIGCHI\\gnome-data\\conversations.csv"
    #infilename = "C:\\Users\\richard\\Desktop\\SIGCHI\\gnomes-data\\20170911_conversations\\conversations_sep.csv"
    infilename = "C:\\Users\\richard\\Dropbox\\SIGCHI\\conversations.csv"

    loadData(infilename)

    speak("by your command")
    speak("loaded "+str(len(conversations))+" conversations")
    while True:
        rand_conversation = random.choice(conversations)
        speakConversation(rand_conversation)
        sys.stdout.flush()
        delaySecs = random.randint(2,10)
        time.sleep(delaySecs)


###############################################################################
if __name__ == "__main__":
    main()