from features.sense import *
import sys, random
from features.date_time import datetime
from features.walter_chat import *

def chat_bot(query):
    if query in command_info:
        speak(listToString(random.choices(info)))

    elif query in command_greet:
        speak(listToString(random.choices(greet)))

    elif query in chat_1:
        speak(listToString(random.choices(chat_1_replay)))

    elif query in chat_2:
        speak(listToString(random.choices(chat_2_replay)))

    elif query in chat_3:
        speak(listToString(random.choices(chat_3_replay)))

    elif query in chat_4:
        speak(listToString(random.choices(chat_4_replay)))

    elif query in chat_5:
        speak(listToString(random.choices(chat_5_replay)))

    elif query in chat_6:
        speak(listToString(random.choices(chat_6_replay)))

    elif query in chat_7:
        speak(listToString(random.choices(chat_7_replay)))

    elif query in chat_8:
        speak(listToString(random.choices(chat_8_replay)))

    elif query in chat_9:
        speak(listToString(random.choices(chat_9_replay)))

    elif query in chat_10:
        speak(listToString(random.choices(chat_10_replay)))

    elif query in chat_11:
        speak(listToString(random.choices(chat_11_replay)))
        
    elif query in command_quit:
        speak(listToString(random.choices(command_quit_replay)))
        sys.exit()
    else:
        return 0

def greetAndWork(query):
    #greet and perform task simultaneously
    #eg- hello walter, what is the temperature?
    #eg- good morning walter, how is the weather?
    if 'hello' in query or 'good morning' in query:
        wishMe()  # greets user
        #replacing unnecessary key words from query
        query = query.replace("hello", "")
        query = query.replace("hi", "")
        query = query.replace("good morning", "")
        query = query.replace("walter", "")
        #correcting mispronounciations
        #sometimes it misunderstands 'Walter' as these: (due to indian accent)
        query = query.replace("water", "")
        query = query.replace("walton", "")
        query = query.replace("wallpaper", "")

    return query

def wishMe():
    #function wishme will wish the user according to the time and weather
   # declaring the hour variable to  get the current hour
    try:
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Hello sir, Good Morning.")
        elif hour >= 12 and hour < 18:
            speak("Hello sir, Good Afternoon.")
        else:
            speak("Hello sir, Good Evening.")
                
    except Exception as e:
        print(e)
