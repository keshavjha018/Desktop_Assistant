# Module webbrowser is used to browse any website/query or open a new tab
import webbrowser
# This os module is used to find/open any folder/application in your system
import os
# ramdom module used to give any random num
import random
import pyautogui
#for jokes
import pyjokes
import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTime, QTimer, QDate, Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
#-----------------------------------------------------------------------------------
from features import weather
from features import chatbot
from features import location
from features import get
from features import google
from features import website
from features import login
from features import date_time
from features import basic
from features import speakthis
#-----------------------------------------------------------------------------------

class walter:
    def __init__(self):
        pass
    
    def open(self,query):
        try:
            website.open_app(query)
        except Exception as e:
            website.open_website(query)
    
    def weather(self,query):
        try:
            val = weather.GetWeather(query)
        except Exception as e:
            val = "Sorry sir i m not able to get it right now"

        return val
    
    def temperature(self, query):
        try:
            val = weather.GetTemperature(query)
        except Exception as e:
            val = "Sorry sir i m not able to get it right now"

        return val
    
    def chatresponse(self,query):
        try:
            val1, val2 = chatbot.chat_bot(query)
            if val2 == 0:
                return val1
        except Exception as e:
            val1 = "Sorry sir, but its not in my data"
        return val1,val2
    
    def howto(self,query):
        try:
            val = google.how_to(query)
        except Exception as e:
            val = "Sorry sir i m not able to get it right now"

        return val
       
    def google(self,query):
        try:
            val = google.googlesearch(query)
        except Exception as e:
            val = "Sorry sir i m not able to get it right now"

        return val

    def near(self, query):
        try:
            val = google.nearby(query)
        except Exception as e:
            val = "Sorry sir i m not able to get it right now"

        return val
    
    def location(self, query):
        try:
            current_loc, target_loc, distance = location.loc(query)
        except Exception as e:
            print(e)
        return current_loc, target_loc, distance

    def my_location(self):
        try:
            city, state, country = location.my_location()
        except Exception as e:
            print(e)
            
        return city, state, country
    
