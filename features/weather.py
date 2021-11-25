from features.location import requests
from bs4 import BeautifulSoup
from features.login import webdriver
from features.get import access


def GetWeather(query):

    chromedriver_path = access().path("chromedriver_path")
    driver = webdriver.Chrome(chromedriver_path)
    driver.minimize_window()
    driver.get("https://www.google.com/search?q=" + query)

    # identify element
    temp = driver.find_element_by_xpath('//*[@id="wob_tm"]')
    sky = driver.find_element_by_xpath('//*[@id="wob_dc"]')
    city = driver.find_element_by_xpath('//*[@id="wob_loc"]')
    ppt = driver.find_element_by_xpath('//*[@id="wob_wc"]/div[1]/div[2]/div[1]')
    humidity = driver.find_element_by_xpath('//*[@id="wob_wc"]/div[1]/div[2]/div[2]')
    Wind = driver.find_element_by_xpath('//*[@id="wob_wc"]/div[1]/div[2]/div[3]')

    #tells weathe in details - like ppt, wind etc
    if 'detail' in query or 'details' in query:
        # get text and print
        val = "The current temperature in " + city.text + " is " + temp.text + "°C," + " and the sky is " + \
            sky.text + ". " + "Some other details are. " + \
            ppt.text + ', ' + humidity.text + ', and ' + Wind.text
        return val

    # tells overall weather only, not in details
    else:
        # get text and print
        val = "The current temperature in " + city.text + " is " + \
            temp.text + "°C," + " and the sky is " + sky.text + ". "
        return val

    driver.close()

def GetTemperature(query):
    if "temperature in" in query:
        url = "https://www.google.com/search?q=" + query
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        temp = "The current temperature there" + " is " + temp

    else:
        url = "https://www.google.com/search?q=" + "temperature"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        temp = "The current temperature at your location is " + temp

    return temp
