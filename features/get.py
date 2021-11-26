import os
import csv
from features.date_time import datetime
from requests.api import patch

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
                    
    def personal_details(self, argument):
        try:
            if os.stat("personal_data.txt").st_size != 0:
                with open("personal_data.txt", 'r') as file:
                    check = csv.reader(file)
                    for row in check:
                        if argument in row[0]:
                            return row[1],row[2]
        except Exception as e:
            print(e)
                    
    def mail_details(self, argument):
        try:
            if os.stat("mail_database.txt").st_size != 0:
                with open("mail_database.txt", 'r') as file:
                    check = csv.reader(file)
                    for row in check:
                        if argument in row[0]:
                            return row[1]
        except Exception as e:
            print(e)

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

    def meet_link(self):
        try:
            curr_lecture = self.lecture()
            return dict_link[curr_lecture], curr_lecture
        except Exception as e:
            print(e)