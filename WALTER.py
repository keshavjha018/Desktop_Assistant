#The current time,date & day will be taken from datetime module
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
import sys
from chatbot import *
#for GUI
import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTime, QTimer, QDate, Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Walter_UI import Ui_Walter
import subprocess

state = "Pleaase Wait..."
chat = []
chatlist = ""


def speak(audio):
    # defining the speak function so that our assistant can speak any string given as input
    engine = pyttsx3.init('sapi5')  # defining the engine to speak given string
    voice = engine.getProperty('voices')
    # seting voice of any inbuilt system voice like David/Zeera
    engine.setProperty('voice', voice[1].id)
    # print(voice[0])     # to know the no of voices in system
    engine.setProperty('rate', 188)  # set the speed of voice
    engine.say(audio)
    print(audio)
    global chat
    chat.append("Walter: " + audio)
    # Runs an event loop until all commands queued up until this method call complete
    engine.runAndWait()

def speakonly(audio):
    #only speaks, without printing
    engine = pyttsx3.init('sapi5')  # defining the engine to speak given string
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)
    engine.setProperty('rate', 188)  # set the speed of voice
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    #function wishme will wish the user according to the time and weather
    # declaring the hour variable to  get the current hour
    hour = int(datetime.datetime.now().hour)
    # declaring the strTime variable to  get the current time according to mearidain
    strTime = datetime.datetime.now().strftime("%I:%M %p")
    if hour >= 0 and hour < 12:
        speak("Hello sir, Good Morning. I am your assistant Walter" )
    elif hour >= 12 and hour < 18:
        speak("Hello sir, Good Afternoon. I am your assistant Walter ")
    else:
        speak("Hello sir, Good Evening. I am your assistant Walter")

class mail():
    def __init__(self, sender_mail):
        # accessing the chromedriver path from path.txt
        self.chromedriver_path = access.path("chromedriver_path")
        # accessing the gmai url from url.txt
        self.gmail_url = access.url("gmail_url")
        # Defining a driver to open chrome driver
        self.driver = webdriver.Chrome(self.chromedriver_path)
        self.driver.get(self.gmail_url)  # feeding the mail link to the driver
        self.sender_mail = sender_mail

    def login(self):
        """
        This is a login function used to login your personal gmail account
        by accessing data directli from the files
        """
        self.user_mail, self.user_password = access.personal_details("brij")
        #accessing the password and email details of owner
        self.enter_mail = self.driver.find_element_by_id(
            "identifierId").send_keys(self.user_mail)
        #identifing the textbox using id of element and typing user mail with the help of send_keys() function
        self.user_mail_next = self.driver.find_element_by_id(
            "identifierNext").click()
        #identifing the next button using id of element and clicking on it with the help of click() function
        # sleep time is given so that the time is given to code whlie next page is loded
        sleep(3)
        self.enter_pass = self.driver.find_element_by_name(
            "password").send_keys(self.user_password)
        #identifing the textbox using name of element and typing user password with the help of send_keys() function
        self.pass_next = self.driver.find_element_by_id("passwordNext").click()
        #identifing the next button using id of element and clicking on it with the help of click() function
        sleep(5)

    def compose(self):
        """
        In this function the email will be composed by adding 
        subject, sender mail and content to the email
        """
        self.driver.find_element_by_css_selector(".aic .z0 div").click()
        #identifing the compose button using css_selector of element and clicking on it with the help of click() function
        sleep(3)
        self.driver.find_element_by_name("to").send_keys(self.sender_mail)
        #identifing the textbox of to(text box where sender mail) using name of element and typing mail with the help of send_keys() function
        speak("What subject should i add?")
        self.subject = self.takecomand()
        sleep(1)
        self.driver.find_element_by_name("subjectbox").send_keys(self.subject)
        #identifing the textbox of subject using name of element and typing subject with the help of send_keys() function
        sleep(3)
        speak("Sir what should i say?")
        self.content = self.takecomand()
        sleep(1)
        self.driver.find_element_by_css_selector(
            ".Ar.Au div").send_keys(self.content)
        #identifing the content textbox using css_selector of element and typing content with the help of send_keys() function

        sleep(5)

    def send(self):
        # The send functions just sends the message
    	self.driver.find_element_by_css_selector(
    	    "tr.btC td:nth-of-type(1) div div:nth-of-type(2) div").click()
        #identifing the send button using css_selector of element and clicking on it with the help of click() function
    	sleep(5)
    	self.driver.close()  # closing the driver

class MainThread(QThread):
    def __init__(self) -> None:
        super(MainThread, self).__init__()

    def run(self):
        wishMe()
        self.task()
    
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
            global chat
            chat.append("User said: " + query)
        except Exception as e:
            state = "Speak again..."
            print(state)
            return "None"
        return query.lower()  # returning the query in lower alphabets

    def task(self):
        # running the while loop infinite times
        while True:
            self.query = self.takecomand()

            #if user asks intro
            if self.query in command_info:
                s = random.choices(info)
                listToStr = ' '.join(map(str, s))
                speak(listToStr)
            
            #if user greets
            elif self.query in command_greet:
                s = random.choices(greet)
                listToStr = ' '.join(map(str, s))
                speak(listToStr)
            
            elif 'open youtube' in self.query or 'open YouTube'in self.query:
                speakonly('Opening Youtube')
                # taking the link of youtube from the folder url.txt using access.py file
                # opening yutube in defult webbrowser
                webbrowser.open_new_tab(access.url("youtube_url"))

            elif 'open google' in self.query:
                speak("Sir, are you looking for any website?")
                ans=self.takecomand()
                if 'yes' in ans:
                    speak("Sir, which website are you looking for?")
                    search=self.takecomand()
                    webbrowser.open_new_tab(search + ".com")
                else:
                    speak("Sir, what should i search for?")
                    search=self.takecomand()
                    webbrowser.open_new_tab(search)

            elif 'open classroom' in self.query:
                webbrowser.open_new_tab(access.url("classroom_url"))

            elif 'play music' in self.query:
                self.music_dir=access.path("music_dir_path")
                self.songs=os.listdir(self.music_dir)
                os.startfile(os.path.join(
                self.music_dir, random.choice(self.songs)))

            elif 'date' in self.query:
                self.today= datetime.date.today()
                self.d2 = self.today.strftime("%B %d, %Y")
                self.day=datetime.datetime.now().strftime("%A")
                speak("Today is " + self.day + '. ' + self.d2)

            elif 'the time' in self.query:
                self.strTime = datetime.datetime.now().strftime("%I %M %p")
                speak("Sir, The time is " + self.strTime)

            elif 'open notepad' in self.query:
                speakonly("Opening Notepad")
                os.startfile(access.path("notepad_path"))

            elif 'open vs code' in self.query:
                speakonly("Opening VS Code")
                self.codepath=access.path("vs_code_path")
                os.startfile(self.codepath)

            elif 'send mail' in self.query:
                try:
                    self.query=self.query.replace("send", "")
                    self.query=self.query.replace("mail", "")
                    self.query=self.query.replace("to", "")
                    self.query=self.query.replace(" ", "")
                    self.to_email=access.mail_details(self.query)
                    self.obj=mail(self.to_email)
                    self.obj.login()
                    self.obj.compose()
                    self.obj.send()
                    speak("Sir, the mail is sent")
                except Exception as e:
                    speak("Sorry sir. I am not able to send right now")

            elif self.query in command_quit:
                s = random.choices(command_quit_replay)
                listToStr = ' '.join(map(str, s))
                speak(listToStr)
                sys.exit()
    
startexecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Walter()
        self.ui.setupUi(self)
        self.ui.run_button.clicked.connect(self.starttask)
        self.ui.Terminate.clicked.connect(self.close)
        
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        lable_time = current_time.toString('hh:mm:ss')
        lable_date = current_date.toString(Qt.ISODate)
        self.ui.Date.setText(lable_date)
        self.ui.Time.setText(lable_time)
        self.ui.state_of_assistant.setText(state)
        global chatlist
        for item in chat:
            if item not in chatlist:
                chatlist = chatlist + item + " \n"

        self.ui.Chat_box.setText(chatlist)
        
    def starttask(self):
        self.ui.movie = QtGui.QMovie("image/Walter bg.gif")
        self.ui.bg_lab.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("image/footer(line).gif")
        self.ui.footer_img.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000) 
        startexecution.start()
        
    # def showquery()

app = QApplication(sys.argv)
friday = Main()
friday.show()
exit(app.exec_())