import datetime

def time():
    # declaring the strTime variable to  get the current time
    return datetime.datetime.now().strftime("%I %M %p")
     
def date():
    return datetime.date.strftime("%B %d, %Y")
    
def day():
    return datetime.datetime.now().strftime("%A")
