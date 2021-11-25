from features import weather
from features import chatbot
from features import location
from features import get
from features import google
from features import open_close
from features import login
from features import date_time
from features import basic
from features import sense
from features import open_close

class walter:
    def __init__(self):
        pass
    
    def open(self,query):
        query = query.replace("open", "")
        query = query.replace("launch", "")
        query = query.replace("my", "")
        query = query.replace("account", "")
        query = query.replace("application", "")
        query = query.replace(" ", "")
        if query in list(open_close.dict_app.keys()):
            open_close.open_app(query)
        else:
            open_close.open_website(query)
    
    def close(self,query):
        query = query.replace("close", "")
        query = query.replace("exit", "")
        query = query.replace("terminate", "")
        query = query.replace(" ", "")
        if query in list(open_close.dict_app.keys()):
            open_close.close_app(query)
        else:
            open_close.close_website()
    
    def weather(self,query):
        try:
            val = weather.GetWeather(query)
        except Exception as e:
            val = "Sorry sir i m not able to get it right now"
        return val
    
    def temperature(self, query):
        try:
            val = weather.GetTemperature(query)
        except Exception as e:
            val = "Sorry sir i m not able to get it right now"

        return val

    def howto(self,query):
        try:
            val = google.how_to(query)
        except Exception as e:
            val = "Sorry sir i m not able to get it right now"

        return val
       
    def google(self,query):
        try:
            val = google.googlesearch(query)
        except Exception as e:
            val = "Sorry sir i m not able to get it right now"
        return val

    def near(self, query):
        try:
            val = google.nearby(query)
        except Exception as e:
            val = "Sorry sir i m not able to get it right now"

        return val
    
    def location(self, query):
        current_loc, target_loc, distance = location.loc(query)
        return current_loc, target_loc, distance

    def my_location(self):
        city, state, country = location.my_location()
        return city, state, country
    
    def time(self):
        return date_time.time()
    
    def send_mail(self,query):
        query = query.replace("send", "")
        query = query.replace("mail", "")
        query = query.replace("to", "")
        query = query.replace(" ", "")
        obj = login.mail()
        obj.login()
        obj.compose(get.access().mail_details(query))
        obj.send()

    def join_meet(self,query):
        obj = login.meet()
        if 'new meet' in query or 'create a meet' in query:
            obj.login()
            obj.creat_meet()
        else:
            a = obj.check_class()
            if a == 0:
                obj.close()
            else:
                obj.login()
                obj.join_link()
                if a == 1:
                    obj.join()
        
