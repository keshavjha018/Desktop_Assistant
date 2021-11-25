import pyttsx3                          # to set the output voice for your desktop assistant
import speech_recognition as sr         # used to get any voice input
from time import sleep

#---------------------------------------------------------------

# sets/updates current state or mode
state = "Speaking..."

# Maintains chatbox
chat = []
chat_prev = []

#--------------------------- For Voice Output -------------------------------------

engine = pyttsx3.init('sapi5')                  # defining the engine to speak given string
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)        # seting voice of any inbuilt system voice like David/Zeera

def speak(audio):
    try:
        # print(voice[0])                       # to know the no of voices in system
        global state
        state = "Speaking..."
        engine.say(audio)
        engine.setProperty('rate', 188)         # set the speed of voice
        print(audio)
        chatWalter(audio)                       # appends the output in chat box at GUI
        engine.runAndWait()                     # Runs an event loop until all commands queued up until this method call complete
    except Exception as e:
        print(e)

#----------------------------- For voice Input --------------------------------------

# Defining function to take the voice as input and converting it to text
def takecomand():
    take = sr.Recognizer()
    # It takes Speech as input from microphone
    with sr.Microphone() as source:
        
        take.adjust_for_ambient_noise(source)           # ignoring the background noise
        
        take.pause_threshold = 0.7                      # seconds of non-speaking audio before a phrase is considered complete
        take.energy_threshold = 500                     # minimum audio energy to consider for recording
        take.dynamic_energy_threshold = True            # adjusts background noise
        global state
        state = "Listening...."
        print(state)
        audio = take.listen(source)
    try:
        state = "Working...."
        print(state)
        query = take.recognize_google(audio, language='en-in')  # Performs speech recognition on "audio_data", using the Google Speech Recognition API.
        
        print("User said :", query)

    except Exception as e:
        state = "Speak again..."
        print(state)
        return "None"
    chatUser(query)
    return query.lower()                                # returning the query in lower alphabets

#-------------------------------------------------------------------------------------

# Updates walter's chat in chatbox (GUI)
def chatWalter(query):
    global chat_prev
    chat_prev = chat.copy()
    chat.append("Walter: " + query + "\n")

# updates user's command in chatbox (GUI)
def chatUser(query):
    global chat_prev
    chat_prev = chat.copy()
    chat.append("User: " + query + "\n")
    sleep(1)
