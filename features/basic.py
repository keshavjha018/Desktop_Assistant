from date_time import datetime
from speakthis import speak

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
            
def listToString(query):
        # initialize an empty string
        str = ""
        # traverse in the string
        for ele in query:
            str += ele
        # return string
        return str
    