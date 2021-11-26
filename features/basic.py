import pyautogui
from time import sleep
import wmi

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
    pyautogui.press("volumemute") #mute the system
    chatWalter("Systems Muted")

def unmute():
    pyautogui.press("volumemute")  # unmute the system
    chatWalter("Systems Unmuted")

def chatWalter(query): #function required for displaying the chat of Walter in chatbox
    global chat_prev    
    chat_prev = chat.copy() #copying the chat list in chat_perv list
    chat.append("Walter: " + query + "\n") #appending the latest query in the chat list

def chatUser(query):  # function required for displaying the chat of User in chatbox
    global chat_prev
    chat_prev = chat.copy()  # copying the chat list in chat_perv list
    chat.append("User: " + query + "\n") #appending the latest query in the chat list
    sleep(1)

def battery():
    c = wmi.WMI()
    t = wmi.WMI(moniker="//./root/wmi")
    batts1 = c.CIM_Battery(Caption='Portable Battery')
    batts = t.ExecQuery('Select * from BatteryFullChargedCapacity')
    for i, b in enumerate(batts):
        full = (b.FullChargedCapacity)
    batts = t.ExecQuery('Select * from BatteryStatus where Voltage > 0')
    for i, b in enumerate(batts):
      rem = (b.RemainingCapacity)
    per = int((rem/full)*100)
    return per