from features.get import access
from features.sense import *
dict_app = {'notepad': 'notepad', 'calculator': 'calc',
            'file': 'explorer', 'paint': 'mspaint', 'terminal': 'cmd', 'vscode': 'Code',
            'chrome': 'chrome'}

# from get import access
# from basic import listToString
# from sence import speak

import random
import webbrowser,os
import keyboard
def open_website(query):
    query = query.replace(" ","")
    # speak(listToString(random.choices([f'Opening {query}', f'Launching {query}'])))
    webbrowser.open_new_tab("www." + query + ".com")

def close_website():
    # speak(listToString(random.choices(['Closing website', 'Termenating website'])))
    keyboard.press_and_release('ctrl + w')
    
def open_app(query):
    # speak(listToString(random.choices([f'Opening {query}', f'Launching {query}'])))
    apps = list(dict_app.keys())
    for app in apps:
        if app in query:
            os.system(f"start {dict_app[app]}")
       
def close_app(query):
    #working on it
    apps = list(dict_app.keys())
    for app in apps:
        if app in query:
            # speak(listToString(random.choices([f'Closing {query}', f'Termenating {query}'])))
            os.system(f"TASKKILL /F /IM {dict_app[app]}.exe")
