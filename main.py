from features import *
from features import walter
from features.speakthis import speak
from features.get import access
from gui import Ui_Walter

class MainThread(QThread):
    def __init__(self) -> None:
        self.x = 1
        super(MainThread, self).__init__()

    def run(self):
        basic.wishMe()
        self.task()

    def task(self):
        # running the while loop infinite times
        while True:
            self.query = speakthis.takecomand()
            #if user chats (conversation)
            chatresponse = chatbot.chat_bot(self.query)

            #if not in chatbot
            #greet and perform task simultaneously - (can run multiple command at once)
            #eg- hello walter, what is the temperature?
            if chatresponse == 0:
                self.query = basic.greetAndWork(self.query)

            if 'open youtube' in self.query or 'launch youtube' in self.query:
                speak(listToString(random.choices(['Opening Youtube', 'Launching Youtube'])))
                # taking the link of youtube from the folder url.txt using access.py file
                # opening youtube in defult webbrowser 
                webbrowser.open_new_tab(access.url("youtube_url"))

            elif 'open google' in self.query:
                speak("Sir, are you looking for any website?")
                ans = speakthis.takecomand()
                if 'yes' in ans:
                    speak("Sir, which website are you looking for?")
                    search = speakthis.takecomand()
                    webbrowser.open_new_tab(search + ".com")
                else:
                    speak("Sir, what should i search for?")
                    search = speakthis.takecomand()
                    webbrowser.open_new_tab(search)

            elif 'open classroom' in self.query:
                webbrowser.open_new_tab(access.url("classroom_url"))

            elif 'date' in self.query:
                date = date_time.date()
                day = date_time.day()
                speak("Today is " + day + '. ' + date)

            elif 'the time' in self.query:
                # declaring the strTime variable to  get the current time according to mearidain
                strTime = date_time.time()
                speak("Sir, The current time is " + strTime)

            elif 'open notepad' in self.query or 'launch notepad' in self.query:
                speak(listToString(random.choices(['Opening Notepad', 'Launching Notepad'])))
                os.startfile(access.path("notepad_path"))

            elif 'open vs code' in self.query or 'launch vs code' in self.query:
                speak(listToString(random.choices(['Opening VS Code', 'Launching VS Code'])))
                self.codepath=access.path("vs_code_path")
                os.startfile(self.codepath)

            #you must have already logged in (in your default browser)
            elif 'twitter' in self.query and 'open' in self.query:
                speak("Opening Twitter..")
                webbrowser.open_new_tab(access.url("twitter_url"))
                
            elif 'instagram' in self.query and 'open' in self.query:
                speak("Opening Instagram..")
                webbrowser.open_new_tab(access.url("instagram_url"))
                
            elif 'github' in self.query and 'open' in self.query:
                speak("Opening Github..")
                webbrowser.open_new_tab(access.url("github_url"))
                
            elif 'linkedin' in self.query and 'open' in self.query:
                speak("Opening LinkedIn..")
                webbrowser.open_new_tab(access.url("linkedin_url"))
                
            elif 'gmail' in self.query and 'open' in self.query:
                speak("Opening Gmail..")
                webbrowser.open_new_tab(access.url("gmail_url"))

            #if not logged in
            elif 'twitter' in self.query and 'login' in self.query:
                walter.()
                
            elif 'screenshot' in self.query or 'take a screenshot' in self.query:
                cwd = os.getcwd()
                pyautogui.screenshot(cwd + r'\image\Screenshot' + str(self.x)+'.png')
                speak("Screenshot is saved as image" + str(self.x))
                self.x += 1

            elif 'temperature' in self.query:
                speak(walter.temperature(self.query))

            elif "weather" in self.query:
                speak(walter.weather(self.query))
                # chat.append("Walter: " + chatmsg2) #prints weather in chatbox

            elif "how to" in self.query:
                speak(walter.howto(self.query))

            elif "search" in self.query:
                self.query = self.query.replace("search", "")
                self.query = self.query.replace(" for ", "")
                self.query = self.query.replace(" about ", "")
                self.query = self.query.replace(" on ", "")
                self.query = self.query.replace("google", "")
                speak("Showing the search results for" + self.query)
                walter.google(self.query)
            
            elif "near" in self.query or 'nearby' in self.query:
                speak(walter.near(self.query))
                # chat.append("Walter: "+ nearby(self.query))   #adding msg to chatbox

            elif "joke" in self.query or 'jokes' in self.query:
                speak(pyjokes.get_joke())
                self.query = self.takecomand()
                while 'one more' in self.query or 'another one' in self.query or 'once more' in self.query:
                    speak(pyjokes.get_joke())
                    self.query = self.takecomand()

            elif 'send mail' in self.query:
                try:
                    self.query=self.query.replace("send", "")
                    self.query=self.query.replace("mail", "")
                    self.query=self.query.replace("to", "")
                    self.query=self.query.replace(" ", "")
                    obj = walter.mail()
                    obj.login()
                    speak("What subject should i add?")
                    self.subject = self.takecomand()
                    speak("Sir what should i say?")
                    self.content = self.takecomand()
                    self.to_email=access.mail_details(self.query)
                    obj.compose(self.subject,self.content,self.to_email)
                    obj.send()
                    speak("Sir, the mail is sent")
                except Exception as e:
                    speak("Sorry sir. I am not able to send right now")
            
            elif 'join meet' in self.query or 'create a meet' in self.query or 'create a new meet' in self.query or 'join my class' in self.query:
                obj = meet()
                if 'new meet' in self.query or 'create a meet' in self.query:
                    speak("Sir please wait a while i am login your mail")
                    obj.login()
                    speak("Creating a new meet")
                    obj.creat_meet()
                else:
                    a = obj.check_class()
                    if a == 0:
                        obj.close()
                    else:
                        obj.login()
                        obj.join_link()
                        if a == 1:
                            obj.join()

            elif "my location" in self.query or "where am i" in self.query or "current location" in self.query:
                try:
                    ci, st, co = walter.my_location()
                    speak(
                        f"Sir, your current location is {ci} city which is in {st} state and country {co}")

                except Exception as e:
                    speak(
                        "Sorry sir, I coundn't fetch your current location. Please try again")

            elif "where is" in self.query or 'location of' in self.query or 'distance of' in self.query:
                self.query = self.query.replace("where","")
                self.query = self.query.replace("is","")
                self.query = self.query.replace("location", "")
                self.query = self.query.replace("from", "")
                self.query = self.query.replace("my", "")
                self.query = self.query.replace("of", "")
                self.query = self.query.replace("distance", "")
                self.query = self.query.replace(" ", "")


                place = self.query
                current_loc, target_loc, distance = walter.location(place)
                city = target_loc["city"]
                state = target_loc["state"]
                country = target_loc["country"]
                # walter.sleep(1)
                try:
                    res = f"{place} is in {state} state of country {country}. It is {distance} km away from your current location"
                    speak(res)
                except:
                    res = "Sorry sir, I couldn't get the location. Please try again"
                    speak(res)

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
        self.ui.state_of_assistant.setText(state)
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
