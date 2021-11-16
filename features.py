import datetime
#The pyttsx3 module is used here to set the output voice for your desktop assistant
import pyttsx3
#The speech recognition module is used to get any voice input from the user
import speech_recognition as sr
#Sleep function is used to stop any process for a while
from time import sleep
# Module webbrowser is used to browse any website/query or open a new tab
import webbrowser
# This os module is used to find/open any folder/application in your system
import os
# ramdom module used to give any random num
import random
# webdriver is used to open the chrome driver
from selenium import webdriver
# access file contain the function to find an path/details/urls in the respective file
import access

#for web scrapping
import requests
from bs4 import BeautifulSoup

from WALTER import speak

def takecomand(self):
        #Defining function to take the voice as input and converting it to text
        take = sr.Recognizer()
        # It takes Speech as input from microphone
        with sr.Microphone() as source:
            take.adjust_for_ambient_noise(source)  # ignoring the background noise
            # seconds of non-speaking audio before a phrase is considered complete
            take.pause_threshold = 0.7
            take.energy_threshold = 300  # minimum audio energy to consider for recording
            global state        
            state = "Listening...."
            print(state)
            audio = take.listen(source)
        try:
            state = "Recognizing...."
            print(state)
            query = take.recognize_google(audio, language='en-in')
            #Performs speech recognition on "audio_data", using the Google Speech Recognition API.
            print("User said :", query)
            # global chat
            # chat.append("User said: " + query)
        except Exception as e:
            state = "Speak again..."
            print(state)
            return "None"
        return query.lower()  # returning the query in lower alphabets

def GetTemperature(query):
    if "temperature in" in query:
        url = "https://www.google.com/search?q=" + query
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div", class_="BNeawe").text
        speak("The current temperature there" + " is " + temp)

    else:
        url = "https://www.google.com/search?q=" + "temperature"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div", class_="BNeawe").text
        speak("The temperature now" + " is " + temp)