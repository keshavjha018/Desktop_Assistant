import os
import csv
import datetime
from requests.api import patch

#-----------------------------------------------------------

#contains meet links
dict_link = {
    "Probability": "http://www.gmail.com",
    "Discrete Mathematics": "https://meet.google.com/qfw-wbgu-iyn",
    "Industrial Social Psychology": "https://meet.google.com/hdj-neib-qju",
    "Design and Analysis of Algorithm": "https://meet.google.com/snn-dzxf-ngd",
    "Computer Architecture Lab": "https://meet.google.com/mjc-masg-rqy",
    "Object Oriented programing": "http://www.gmail.com",
    "Discrete Mathematics Tutorial": "https://meet.google.com/qfw-wbgu-iyn",
    "Design and Analysis of Algorithm Lab": "https://meet.google.com/snn-dzxf-ngd",
    "Object Oriented programing Lab": "http://www.gmail.com",
    "Probability Tutorial": "http://www.gmail.com",
    "break": None, "Holiday": None, "No lecture": None}

class access:
    #gets path of application from path.text
    def path(self,argument):
        try:
            if os.stat("path.txt").st_size != 0:
                with open("path.txt", 'r') as file:
                    check = csv.reader(file)
                    for row in check:
                        if argument in row[0]:
                            return row[1]
        except Exception as e:
            print(e)

    #fetches url from url.txt                
    def url(self, argument):
        try:
            if os.stat("url.txt").st_size != 0:
                with open("url.txt", 'r') as file:
                    check = csv.reader(file)
                    for row in check:
                        if argument in row[0]:
                            return row[1]
        except Exception as e:
            print(e)

    # fetches personal details from personal_data.txt               
    def personal_details(self, argument):
        try:
            if os.stat("my_mail_details.txt").st_size != 0:
                with open("my_mail_details.txt", 'r') as file:
                    check = csv.reader(file)
                    for row in check:
                        if argument in row[0]:
                            return row[1],row[2]
        except Exception as e:
            print(e)

    # fetches mail details from mail_database.txt                
    def mail_details(self, argument):
        try:
            if os.stat("mail_details.txt").st_size != 0:
                with open("mail_details.txt", 'r') as file:
                    check = csv.reader(file)
                    for row in check:
                        if argument in row[0]:
                            return row[1]
        except Exception as e:
            print(e)

    # finds the current slot number (to join the class) 
    # using current date,time and day
    def get_time_slot(self):
        hour = int(datetime.datetime.now().hour)
        minute = int(datetime.datetime.now().minute)
        if hour < 9:
            return 0
        elif 9 <= hour < 10:
            return 1
        elif 10 <= hour < 11:
            return 2
        elif 11 <= hour < 12:
            return 3
        elif 12 <= hour < 13:
            return 4
        elif 13 <= hour < 14:
            if minute < 15:
                return 5
            else:
                return 6
        elif 14 <= hour < 15:
            return 7
        else:
            return 0

    def get_day(self):
        return datetime.datetime.now().strftime("%A")

    #finds lecture from timetable.txt
    def lecture(self):
        try:
            time_slot = self.get_time_slot()
            day = self.get_day()
            # day = "Sunday"
            # time_slot = 0
            if time_slot == 0:
                return "No lecture"
            else:
                if os.stat("timetable.txt").st_size != 0:
                    with open("timetable.txt", 'r') as file:
                        check = csv.reader(file)
                        for row in check:
                            if day in row[0]:
                                return row[time_slot]
        except Exception as e:
            print(e)

    # fetches meet link from dictionary : dict_link
    def meet_link(self):
        try:
            curr_lecture = self.lecture()
            return dict_link[curr_lecture], curr_lecture
        except Exception as e:
            print(e)
