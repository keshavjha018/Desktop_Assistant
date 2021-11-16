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
    # global chat
    # chat.append("Walter: " + audio)
    # Runs an event loop until all commands queued up until this method call complete
    engine.runAndWait()

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
        self.user_mail, self.user_password = access.personal_details("Your_name")
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
    	self.driver.find_element_by_css_selector("tr.btC td:nth-of-type(1) div div:nth-of-type(2) div").click()
        #identifing the send button using css_selector of element and clicking on it with the help of click() function
    	sleep(5)
    	self.driver.close()  # closing the driver