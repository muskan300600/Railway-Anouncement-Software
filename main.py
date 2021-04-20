import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text,filename):
    '''This function '''
    pass

def mergeAudios(audios):
    '''This function returns pydubs audio segment'''
    pass

def generateSkeleton():
    # 1st part
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")
    
    # 2nd part
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")
    
    # 3rd part
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")
    
    # 4th part
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # 5th part
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3")
    
    # 6th part
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3")
    

def generateAnnouncement(filename):
    pass

if __name__ == '__main__':
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now generating Announcement")
    generateAnnouncement("announce_hindi.xlsx")




