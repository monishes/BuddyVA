import pyttsx3
from decouple import config

USERNAME=config('USER')
BOTNAME=config('BOTNAME')

#Initializing the engine using pyttsx3 module. sapi5 is a Microsoft Speech API which allows us to access different voices.
engine=pyttsx3.init('sapi5')

#To set the Volume and Rate of the speech Engine
engine.setProperty('rate',190)
engine.setProperty('volume',1.0)

#To initialize the voice of our speech engine
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#Enabling the Speech Funciton#

#Converting Text to Speech

def speak(text):
    engine.say(text)
    engine.runAndWait()


#Opening Function - At the start of the Virtual Assistant
from datetime import datetime

def greetme():
    hour=datetime.now.hour
    if(hour>=6) and (hour<12):
        speak(f"Good Morning {USERNAME}")
    elif (hour>=12) and (hour<16):
        speak(f"Good Afternoon {USERNAME}")
    elif (hour>=16) and (hour<19):
        speak(f"Good Evening {USERNAME}")
    speak(f"How may I assist you sir?")


#Listening Commands from User

import speech_recognition as sr
from random import choice
from utils import opening_text

def user_commands():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening to your commands ......')
        audio=r.listen(source)

    try:
        print('Recognizing .....')
        query=r.recognize_google(audio,language="en-in")
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour=datetime.now().hour
            if hour>=21 and hour<6:
                speak("Good Night sir, Take Care!")
            else:
                hour=datetime.now().hour
                if hour>=21 and hour<6:
                    speak("Have a Good Day sir !")
            exit()
    except Exception:
        speak("Sorry sir, I couldnt't quite get that, Could it repeat it again sir ?")
        query='None'
    return query
