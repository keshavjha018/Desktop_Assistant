# from features.get import access
dict_app = {'notepad': 'notepad', 'calculator': 'calc',
            'file': 'explorer', 'paint': 'mspaint', 'terminal': 'cmd', 'vscode': 'Code',
            'chrome': 'chrome'}

# from get import access
# from basic import listToString
from features import sense

import random
import webbrowser,os
import keyboard
#function to open a website
def open_website(query):
    query = query.replace(" ", "")  # removing unwanted space
    sense.speak(sense.listToString(random.choices([f'Opening {query}', f'Launching {query}'])))
    # adding www and .com to website name
    webbrowser.open_new_tab("www." + query + ".com") #opening website in new tab

# function to close website
def close_website():
    sense.speak(sense.listToString(random.choices(
        ['Closing website', 'Termenating website'])))
    keyboard.press_and_release('ctrl + w')  # shortcut to close a window

#function to open an app
def open_app(query):
    sense.speak(sense.listToString(random.choices(
        [f'Opening {query}', f'Launching {query}'])))
    apps = list(dict_app.keys())  # defining dictionary keys to a list
    for app in apps:  # for loop to search
        if app in query:  # if we find the desired app than open it
            # open the app using os features
            os.system(f"start {dict_app[app]}")


# function to close an app
def close_app(query):
    #working on it
    apps = list(dict_app.keys())  # defining dictionary keys to a list
    for app in apps:  # for loop to search
        if app in query:
            sense.speak(sense.listToString(random.choices([f'Closing {query}', f'Termenating {query}'])))
            os.system(f"TASKKILL /F /IM {dict_app[app]}.exe")  # close the app
