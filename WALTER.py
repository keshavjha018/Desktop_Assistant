#---------------------------------For Features---------------------------------------
# to import chatbot & date_time from features folder
from features import chatbot, date_time
from features import walter  # to import walter from features folder
from features.sense import *  # to import * from features.sense folder
import os
import sys
import pyjokes  # To Import Jokes from pyjokes module
#---------------------------------For GUI -------------------------------------------
import PyQt5
# to import QTime, QTimer, QDate, Qt from PyQt5.QtCore module
from PyQt5.QtCore import QTime, QTimer, QDate, Qt
# to import QtWidgets, QtCore, QtGui from PyQt5 module
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *  # to import * from PyQt5.QtWidgets module
from PyQt5.QtCore import *  # to import * from PyQt5.QtCore module
from PyQt5.QtGui import *  # to import * from PyQt5.QtGui module
from PyQt5.uic import loadUiType  # to import loadUiType from PyQt5.uic module
from Walter_UI import Ui_Walter  # to import UI_Walter from Waltur_UI module
#------------------------------------------------------------------------------------
class MainThread(QThread):
    def _init_(self) -> None:
        self.x = 1
        super(MainThread, self).__init__()

    def run(self):
        self.obj = walter()
        chatbot.wishMe()  # Code to get user welcome greetings from Walter
        self.task()  # code to say to do it yourself as walter is started

    def task(self):
        # running the while loop infinite times
        while True:
            self.query = takecomand()  # walter takes the input from using py.audio
            # if user chats (conversation)
            chatresponse = chatbot.chat_bot(self.query)  # response form chatbot

            # if not in chatbot
            # greet and perform task simultaneously - (can run multiple command at once)
            # eg- hello walter, what is the temperature?

            if chatresponse == 0:
                # if input is not given it will greet user and ask if any work is there
                self.query = chatbot.greetAndWork(self.query)

            if 'open' in self.query or 'launch' in self.query:  # to launch application/website
                self.obj.open(self.query)  # to execute the query command

            # to close, exit or terminate the application/website
            elif 'close' in self.query or 'exit' in self.query or 'terminate' in self.query:
                self.obj.close(self.query)  # to execute the query command

            elif 'date' in self.query:  # walter telling us present day's date
                speak("Today is " + date_time.day() + ', ' + date_time.date())

            elif 'the time' in self.query:  # walter telling us current time
                speak("Sir, The current time is " + date_time.time())
                
            elif 'do' in self.query or 'evaluate' in self.query or 'calculate' in self.query:
                speak(self.obj.calculate(self.query))

            # user giving command to walter to take screenshot
            elif 'screenshot' in self.query or 'take a screenshot' in self.query:
                cwd = os.getcwd()
                # destination where walter will be saving the screenshot
                pyautogui.screenshot(cwd + r'\image\Screenshot' + str(self.x)+'.png')
                # walter giving name to screenshot in numerical value
                speak("Screenshot is saved as image" + str(self.x))
                self.x += 1

            elif 'temperature' in self.query:  
                # command to get temperature information from walter
                speak(self.obj.temperature(self.query))

            elif "weather" in self.query:
                # command to get weather information from walter
                speak(self.obj.weather(self.query))

            elif "how to" in self.query:  # giving walter input in format how to " ------------ "
                speak(self.obj.howto(self.query))

            elif "search" in self.query:  # giving walter input to search " ---------------- "
                speak(self.obj.google(self.query))

            # giving walter input to search nearby " --------- " ex:- hotels, parks, gas station, dentist, etc
            elif "near" in self.query or 'nearby' in self.query:
                speak(self.obj.near(self.query))

            elif "joke" in self.query or 'jokes' in self.query:  # giving command to walter to tell a joke
                speak(pyjokes.get_joke())
                self.query = takecomand()
                # giving command to walter to tell another joke
                while 'one more' in self.query or 'another one' in self.query or 'once more' in self.query:
                    speak(pyjokes.get_joke())
                    self.query = takecomand()

            elif 'send mail' in self.query:  # giving walter the access to email to send email
                try:
                    self.obj.send_mail(self.query)
                    # if the email was send successfully, his output will be "Sir, the email is send'
                    speak("Sir, the mail is sent")
                except Exception as e:
                    # due to some technical error if walter is unable to send email, his output will be 'Sorry sir. I am not able to send right now'
                    speak("Sorry sir. I am not able to send right now")

            # commands to walter to do google meet related things
            elif 'join meet' in self.query or 'create a meet' in self.query or 'create a new meet' in self.query or 'join my class' in self.query:
                try:
                    self.obj.join_meet(self.query)
                except Exception as e:
                    # this will be the output if he couldnt perform the things due to technical error
                    speak("Sorry sir. I am not able to join meet right now")

            # giving command to walter to give our geoloaction by tracking your ip address
            elif "my location" in self.query or "where am i" in self.query or "current location" in self.query:
                try:
                    ci, st, co = self.obj.my_location()
                    speak(
                        f"Sir, your current location is {ci} city which is in {st} state and country {co}")

                except Exception as e:
                    # expected output if he is unable to fetch our current location
                    speak("Sorry sir, I coundn't fetch your current location. Please try again")

            # command to walter to locate a geolocation and tell its distance from users location
            elif "where is" in self.query or 'location of' in self.query or 'distance of' in self.query:
                current_loc, requested_loc, distance = self.obj.location(self.query)
                #accessing the city,state & country form dictonary requested_loc
                city = requested_loc["city"] 
                state = requested_loc["state"]
                country = requested_loc["country"]
                try:
                    speak(f"{self.query} is in {state} state of country {country}. It is {distance} km away from your current location")
                except:
                    # expected output due to technical error
                    speak("Sorry sir, I couldn't get the location. Please try again")

            # to give us information on battey status and remaining battery
            elif "battery status" in self.query or "remaining battery" in self.query:
                speak(str(self.obj.battery_status()))

            elif "set alarm" in self.query:  # instructions to set alarm
                try:
                    self.obj.set_alarm(self.query)
                except Exception as e:
                    # output due to technical error
                    speak("Sorry sir, i am not able to set the alarm.")

startexecution = MainThread()

class Main(QMainWindow):  # It is the thread from which the Python interpreter was started
    def __init__(self):
        super().__init__()
        self.ui = Ui_Walter()  # walter User Interface
        self.ui.setupUi(self)  # setup of walter
        self.ui.run_button.clicked.connect(self.starttask)  # run button in Water UI
        self.ui.Terminate.clicked.connect(self.close)  # Terminate button in UI

    def showText(self):  # Fun to show text in GUI
        current_time = QTime.currentTime()  # shown current time in Walter UI
        current_date = QDate.currentDate()  # shown current date in Walter UI
        # time format shown in Walter UI
        lable_time = current_time.toString('hh:mm:ss')
        # time format shown in  string form in Walter UI
        lable_date = current_date.toString(Qt.ISODate)
        self.ui.Date.setText(lable_date) #displaying the date on GUI Screen
        self.ui.Time.setText(lable_time)  # displaying the time on GUI Screen
        # displaying the state of walter on GUI Screen eg. Speaking...., Working...., etc.
        self.ui.state_of_assistant.setText(listToString(state))
        for item in chat:
            global chat_prev
            if len(chat) != len(chat_prev):
                self.res = listToString(chat[len(chat) - 1]) #accessing the latest element appendend in list
                self.ui.Chat_box.append(self.res) #appending the latest element ot the GUI chatbox
                chat_prev.append(self.res) #appending the latest element ot the the list chat_prev

    def starttask(self):  #fun to start the program execution
        # Live Image used in program
        self.ui.movie = QtGui.QMovie("image/Walter bg.gif")
        self.ui.bg_lab.setMovie(self.ui.movie) #seting the movie as the gis will also move
        self.ui.movie.start() 
        self.ui.movie = QtGui.QMovie("image/footer(line).gif") #another live image
        self.ui.footer_img.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self) #seting timer
        timer.timeout.connect(self.showText) #calling the show function so that live time and date are updated
        timer.start(1000)  # starting timer till 1000 seconds
        startexecution.start() 

app = QApplication(sys.argv) 
friday = Main()
friday.show()
exit(app.exec_())
