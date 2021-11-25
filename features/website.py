dict_app = {'notepad': 'notepad', 'calculator': 'calc',
            'file explorer': 'explorer', 'paint': 'mspaint.exe', 'command promopt': 'cmd', 'vs code': 'Code',
            'chrome': 'chrome'}

from get import access
from basic import listToString,speak
import random
import webbrowser,os
def open_website(query):
    query = query.replace("open", "")
    query = query.replace("launch", "")
    query = query.replace("my", "")
    query = query.replace("account", "")
    query = query.replace(" ","")
    webbrowser.open_new_tab("www." + query + ".com")

def open_app(query):
    query = query.replace("open", "")
    query = query.replace("launch", "")
    query = query.replace("my", "")
    query = query.replace("application", "")
    speak(listToString(random.choices([f'Opening {query}', f'Launching {query}'])))
    apps = list(dict_app.keys())
    for app in apps:
        if app in query:
            os.system(f"start {dict_app[app]}")
            
def close_app(query):
    
