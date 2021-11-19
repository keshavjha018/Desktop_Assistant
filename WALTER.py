from features import *

state = "Please Wait..."
chat = []
chatlist = ""

def speak(audio):
    # defining the speak function so that our assistant can speak any string given as input
    engine = pyttsx3.init('sapi5')  # defining the engine to speak given string
    voice = engine.getProperty('voices')
    # seting voice of any inbuilt system voice like David/Zeera
    engine.setProperty('voice', voice[0].id)
    # print(voice[0])     # to know the no of voices in system
    engine.setProperty('rate', 188)  # set the speed of voice
    engine.say(audio)
    print(audio)
    global chat
    chat.append("Walter: " + audio)
    # Runs an event loop until all commands queued up until this method call complete
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

class MainThread(QThread):
    def __init__(self) -> None:
        self.x = 1
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
            take.energy_threshold = 500  # minimum audio energy to consider for recording
            global state        
            state = "Listening...."
            print(state)
            audio = take.listen(source)
        try:
            state = "Working...."
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
        global chat
        while True:
            self.query = self.takecomand()

            greet(self.query)   
            
            if 'open youtube' in self.query or 'open YouTube'in self.query:
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
                
            elif 'screenshot' in self.query or 'take a screenshot' in self.query:
                cwd = os.getcwd()
                pyautogui.screenshot(cwd + r'\Screenshot' + str(self.x)+'.png')
                self.x += 1
                sleep(2)  # to exit from program after 2 seconds

            elif 'temperature' in self.query:
                chat.append("Walter: "+GetTemperature(self.query))

            elif "weather" in self.query:
                GetWeather(self.query)
                # chat.append("Walter: " + chatmsg2) #prints weather in chatbox

            elif "how to" in self.query:
                howto(self.query)

            elif "search" in self.query:
                speak("Showing the search results")
                googlesearch(self.query)

            elif "near" in self.query or 'nearby' in self.query:
                chat.append("Walter: "+ nearby(self.query))   #adding msg to chatbox

            elif 'send mail' in self.query:
                try:
                    self.query=self.query.replace("send", "")
                    self.query=self.query.replace("mail", "")
                    self.query=self.query.replace("to", "")
                    self.query=self.query.replace(" ", "")
                    self.to_email=access.mail_details(self.query)
                    self.obj=mail(self.to_email)
                    self.obj.login()
                    speak("What subject should i add?")
                    self.subject = self.takecomand()
                    speak("Sir what should i say?")
                    self.content = self.takecomand()
                    self.obj.compose(self.subject,self.content)
                    self.obj.send()
                    speak("Sir, the mail is sent")
                except Exception as e:
                    speak("Sorry sir. I am not able to send right now")

            elif self.query in command_quit:
                speak(' '.join(map(str, random.choices(command_quit_replay))))
                speakonly("3")
                speakonly("2")
                speakonly("1")
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
