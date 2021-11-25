import pyautogui
from time import sleep

state = ["Speaking..."]
chat = []
chat_prev = []
def listToString(query):
    # initialize an empty string
    str = ""
    # traverse in the string
    for ele in query:
        str += ele
    # return string
    return str
    
def mute():
    pyautogui.press("volumemute")
    chatWalter("Systems Muted")

def unmute():
    pyautogui.press("volumemute")
    chatWalter("Systems Unmuted")

def chatWalter(query):
    global chat_prev
    chat_prev = chat.copy()
    chat.append("Walter: " + query + "\n")

def chatUser(query):
    global chat_prev
    chat_prev = chat.copy()
    chat.append("User: " + query + "\n")
    sleep(1)
