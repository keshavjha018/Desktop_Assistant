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

def battery():
    c = wmi.WMI()
    t = wmi.WMI(moniker = "//./root/wmi")

    batts1 = c.CIM_Battery(Caption = 'Portable Battery')
    batts = t.ExecQuery('Select * from BatteryFullChargedCapacity')
    for i, b in enumerate(batts):
        full=(b.FullChargedCapacity)

    batts = t.ExecQuery('Select * from BatteryStatus where Voltage > 0')
    for i, b in enumerate(batts): 
      rem=(b.RemainingCapacity)
    
    per=int((rem/full)*100)
    return per
   