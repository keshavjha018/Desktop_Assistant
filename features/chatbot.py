from features.sence import *
from features.basic import listToString
from features.date_time import datetime
command_info = ['who are you', 'what is your name',
                'what are you', 'tell me about yourself']
info = ['Sir, i am your desktop assistant, My name is walter. What can i do for you',
        'sir, I am walter. Your desktop assistant. Happy to see you.']

command_greet = ['hello walter',
                 'are you there walter', 'are you there', 'hello']
greet = ['Hello sir, how may i help you?',
         'Hello sir, I am here for your help', 'Yes sir, how may i help you']

command_quit = ['close the program', 'quit the program', 'terminate the program', 'exit the program'
                'close program', 'quit program', 'terminate program', 'exit program', 'close', 'quit', 'exit', 'terminate yourself']
command_quit_replay = ['Closing the program', 'Quiting the program',
                       'Terminating the program', 'Exiting the program']

chat_1 = ['good morning walter', 'morning walter', 'good morning']
chat_1_replay = ['Good morning sir. I hope your day will be good',
                 'Good morning sir, how may i help you?', 'Good morinng sir, happy to see you again']

chat_2 = ['thankyou walter', 'thank you',
          'good job', 'good job walter', 'nice job']
chat_2_replay = ['Your welcome sir.', 'My pleasure.', 'Happy to help, sir']

chat_3 = ['you are an idiot', 'what had you done', "are you crazy",
          "shut up", 'you are stupid', 'are you an idiot', 'you are idiot']
chat_3_replay = ['Sorry sir, I apologize',
                 'Sorry sir, I am still learning.', 'Sorry sir']

chat_4 = ['nice work', 'nice work walter', 'good work', "it's awesome"]
chat_4_replay = ['Thank you sir.',
                 'Nice to hear from you sir.', 'My pleasure to help you.']

chat_5 = ['how are you']
chat_5_replay = ['I am fine sir,what about you']

chat_6 = ['i am fine', 'thanks for asikng']
chat_6_replay = ['Oh! nice to hear from you sir']

chat_7 = ['good afternoon walter', 'good afternoon']
chat_7_replay = ['Sir,I hope your day will be good',
                 'Sir, how may i help you?', 'Sir, happy to see you again']

chat_8 = ['how can you help me', 'why i should take your help']
chat_8_replay = ['Sir, i am a your assistant having various features',
                 'Sir, i can automate your variously done daily tasks']

chat_9 = ['who created you', 'who is your creator']
chat_9_replay = [
    'Sir, i am created by students of Indian Institute of Information and Technology Dharwad',
    'Sir, i am a Python project created by students of Indian Institute of Information and Technology Dharwad']

chat_10 = ['what can you do', 'what are your features',
           'what can you do for me', 'what are your functionality']
chat_10_replay = ['Sir, i can do many task like showing weather,playing music,sending mails,opening social media websites and many more',
                  'Sir, my fetures are finding current temperature of any location,find any place,searching in google,show nearby places like hotels,restaurants etc.'
                  'Sir, i can do functionality like showing weather,find any place,launching any local applications like notepad,chrome,firefox etc.']

chat_11 = ['why are you created']
chat_11_replay = ['Sir, i am created to make your daily tasks easy']

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
        speak(listToString(random.choices(command_quit_replay)) + " in 3 seconds")
        speak("3" + " 2" + " 1")
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
