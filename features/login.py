from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from speakthis import speak
from get import access
class log():
    def __init__(self):
        opt = Options()
        opt.add_argument("--disable-extensions")
        # Pass the argument 1 to allow and 2 to block
        opt.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 1,
            "profile.default_content_setting_values.notifications": 2
        })
        # accessing the chromedriver path from path.txt
        self.chromedriver_path = access.path("chromedriver_path")
        # accessing the sign in url from url.txt
        self.sign_in = access.url("sign_in_url")
        # Defining a driver to open chrome driver
        self.driver = webdriver.Chrome(chrome_options=opt, executable_path=self.chromedriver_path)
        self.driver.get(self.sign_in)  # feeding the sign in link to the driver
        sleep(1)

    def login(self):
        """
        This is a login function used to login your personal gmail account
        by accessing data directli from the files
        """
        try:
            self.user_mail, self.user_password = access.personal_details(
                "your_name")
            #accessing the password and email details of owner
            self.enter_mail = self.driver.find_element_by_id("identifierId")
            self.enter_mail.send_keys(self.user_mail)
            #identifing the textbox using id of element and typing user mail with the help of send_keys() function
            self.enter_mail.send_keys(Keys.RETURN)
            #pressing Enter key using Keys function
            # sleep time is given so that the time is given to code whlie next page is loded
            sleep(3)
            self.enter_pass = self.driver.find_element_by_name("password")
            self.enter_pass.send_keys(self.user_password)
            #identifing the textbox using name of element and typing user password with the help of send_keys() function
            self.enter_pass.send_keys(Keys.RETURN)
            sleep(3)
        except Exception as e:
            print(e)

    def close(self):
        self.driver.close()

class mail(log):
    def compose(self, subject, content, reciver_mail):
        """
        In this function the email will be composed by adding 
        subject, sender mail and content to the email
        """
        try:
            self.driver.get(access.url("gmail_url"))
            self.subject = subject
            self.content = content
            self.reciver_mail = reciver_mail
            self.driver.find_element_by_css_selector(".aic .z0 div").click()
            #identifing the compose button using css_selector of element and clicking on it with the help of click() function
            sleep(3)
            self.driver.find_element_by_name("to").send_keys(self.reciver_mail)
            #identifing the textbox of to(text box where sender mail) using name of element and typing mail with the help of send_keys() function
            self.driver.find_element_by_name("subjectbox").send_keys(self.subject)
            #identifing the textbox of subject using name of element and typing subject with the help of send_keys() function
            sleep(3)
            self.driver.find_element_by_css_selector(
                ".Ar.Au div").send_keys(self.content)
            #identifing the content textbox using css_selector of element and typing content with the help of send_keys() function
            sleep(3)
        except Exception as e:
            print(e)

    def send(self):
        try:
            # The send functions just sends the message
            self.driver.find_element_by_css_selector(
                "tr.btC td:nth-of-type(1) div div:nth-of-type(2) div").click()
            #identifing the send button using css_selector of element and clicking on it with the help of click() function
            sleep(2)
        except Exception as e:
            print(e)    
        self.driver.close()  # closing the driver

class meet(log):
    def creat_meet(self):
        try:
            self.driver.maximize_window()
            self.driver.get("https://meet.google.com/")  # link to open google meet
            link = self.driver.find_element_by_xpath("//span[@jsname='V67aGc']")
            link.click()
            link = self.driver.find_element_by_xpath(
                "//li[@aria-label='Start an instant meeting']")
            link.click()
        except Exception as e:
            print(e)

    def check_class(self):
        val = 0
        try:
            self.curr_meet_link, self.lecture = access.meet_link()
            # self.driver.get(self.curr_meet_link)
            if self.lecture == None:
                speak(
                    "Sorry sir, but according to my data you dont have any current lecture at this time")
                sleep(4)
                val = 0

            else:
                if self.lecture == "break" or self.lecture == "Holiday" or self.lecture == "No lecture":
                    speak(f"Sir currently you have {self.lecture}")
                    val =  0

                else:
                    speak(f"Sir currently you have {self.lecture} class")
                    if self.curr_meet_link == None:
                        speak("Sir my data dose not contain this class link")
                        val =  0

                    elif self.curr_meet_link == "http://www.gmail.com":
                        speak("Sir I don't have the meet link so please check in your mail")
                        sleep(4)

                    else:
                        val =  1
        except Exception as e:
            val = 0
            
        return val

    def join_link(self):
        self.driver.get(self.curr_meet_link)

    def join(self):
        try:
            speak("joining the class")
            self.driver.maximize_window()
            sleep(2)
            self.driver.find_element_by_css_selector(
                ".U26fgb.JRY2Pb.mUbCce.kpROve.yBiuPb.y1zVCf.HNeRed.M9Bg4d").click()
            sleep(2)
            self.driver.find_element_by_css_selector(
                ".U26fgb.JRY2Pb.mUbCce.kpROve.yBiuPb.y1zVCf.HNeRed.M9Bg4d").click()
            sleep(1)
            self.driver.find_element_by_css_selector(
                ".NPEfkd.RveJvd.snByac").click()
        except Exception as e:
            print(e)

#if user has not already logged in
def twitterlogin():
    speak("Opening Twitter..")
    chromedriver_path = access().path("chromedriver_path")
    driver = webdriver.Chrome(chromedriver_path)
    driver.get("https://www.twitter.com/login")

    username, password = access().personal_details("twitter")

    sleep(4)
    userNameBox = driver.find_element_by_name('username')
    userNameBox.send_keys(username)
    userNameBox.send_keys(Keys.RETURN)
    sleep(4)
    passwordBox = driver.find_element_by_name('password')
    passwordBox.send_keys(password)
    passwordBox.send_keys(Keys.RETURN)
