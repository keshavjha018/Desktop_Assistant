#---------------------------------For Features----------------------------------------
from features import chatbot,date_time,sense,get
from features import walter
from features.basic import listToString
from features.sense import *
from features.get import os
from features.chatbot import sys
#---------------------------------For GUI -------------------------------------------
import PyQt5
from PyQt5.QtCore import QTime, QTimer, QDate, Qt
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from Walter_UI import Ui_Walter
#-----------------------------------------------------------------------------------
#for jokes
import pyjokes

class MainThread(QThread):
    def __init__(self) -> None:
        self.x = 1
        super(MainThread, self).__init__()

    def run(self):
        self.obj = walter()
        chatbot.wishMe()
        self.task()

    def task(self):
        # running the while loop infinite times
        while True:
            self.query = takecomand()
            # if user chats (conversation)
            chatresponse = chatbot.chat_bot(self.query)

            # if not in chatbot
            # greet and perform task simultaneously - (can run multiple command at once)
            # eg- hello walter, what is the temperature?
            if chatresponse == 0:
                self.query = chatbot.greetAndWork(self.query)

            if 'open' in self.query or 'launch' in self.query:
                self.obj.open(self.query)
                
            elif 'close' in self.query or 'exit' in self.query or 'terminate' in self.query:
                self.obj.close(self.query)
            
            elif 'date' in self.query:
                speak("Today is " + date_time.day() + ' ,' + date_time.date())

            elif 'the time' in self.query:
                # declaring the strTime variable to  get the current time according to mearidain
                speak("Sir, The current time is " + self.obj.time())
                
            elif 'screenshot' in self.query or 'take a screenshot' in self.query:
                cwd = os.getcwd()
                pyautogui.screenshot(cwd + r'\image\Screenshot' + str(self.x)+'.png')
                speak("Screenshot is saved as image" + str(self.x))
                self.x += 1

            elif 'temperature' in self.query:
                speak(self.obj.temperature(self.query))

            elif "weather" in self.query:
                speak(self.obj.weather(self.query))
                # chat.append("Walter: " + chatmsg2) #prints weather in chatbox

            elif "how to" in self.query:
                speak(self.obj.howto(self.query))

            elif "search" in self.query:
                speak(self.obj.google(self.query))
            
            elif "near" in self.query or 'nearby' in self.query:
                speak(self.obj.near(self.query))
                # chat.append("Walter: "+ nearby(self.query))   #adding msg to chatbox

            elif "joke" in self.query or 'jokes' in self.query:
                speak(pyjokes.get_joke())
                self.query =sense.takecomand()
                while 'one more' in self.query or 'another one' in self.query or 'once more' in self.query:
                    speak(pyjokes.get_joke())
                    self.query = sense.takecomand()

            elif 'send mail' in self.query:
                try:
                    self.obj.send_mail(self.query)
                    speak("Sir, the mail is sent")
                except Exception as e:
                    speak("Sorry sir. I am not able to send right now")
            
            elif 'join meet' in self.query or 'create a meet' in self.query or 'create a new meet' in self.query or 'join my class' in self.query:
                try:
                    self.obj.join_meet(self.query)
                except Exception as e:
                    speak("Sorry sir. I am not able to join meet right now")

            elif "my location" in self.query or "where am i" in self.query or "current location" in self.query:
                try:
                    ci, st, co = self.obj.my_location()
                    speak(
                        f"Sir, your current location is {ci} city which is in {st} state and country {co}")

                except Exception as e:
                    speak("Sorry sir, I coundn't fetch your current location. Please try again")

            elif "where is" in self.query or 'location of' in self.query or 'distance of' in self.query:
                current_loc, target_loc, distance = self.obj.location(self.query)
                city = target_loc["city"]
                state = target_loc["state"]
                country = target_loc["country"]
                try:
                    res = f"{self.query} is in {state} state of country {country}. It is {distance} km away from your current location"
                    speak(res)
                except:
                    res = "Sorry sir, I couldn't get the location. Please try again"
                    speak(res)

            #battery status
            elif "battery status" in self.query or "remaining battery" in self.query:
                speak("battery remaining "+self.obj.battery_status()+"%")         

startexecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Walter()
        self.ui.setupUi(self)
        self.ui.run_button.clicked.connect(self.starttask)
        self.ui.Terminate.clicked.connect(self.close)
        
    def showText(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        lable_time = current_time.toString('hh:mm:ss')
        lable_date = current_date.toString(Qt.ISODate)
        self.ui.Date.setText(lable_date)
        self.ui.Time.setText(lable_time)
        self.ui.state_of_assistant.setText(listToString(state))
        for item in chat:
            global chat_prev
            if len(chat) != len(chat_prev):
                self.res = listToString(chat[len(chat) - 1])
                self.ui.Chat_box.append(self.res)
                chat_prev.append(self.res)
        
    def starttask(self):
        self.ui.movie = QtGui.QMovie("image/Walter bg.gif")
        self.ui.bg_lab.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("image/footer(line).gif")
        self.ui.footer_img.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showText)
        timer.start(1000) 
        startexecution.start()
        
    # def showquery()

app = QApplication(sys.argv)
friday = Main()
friday.show()
exit(app.exec_())
