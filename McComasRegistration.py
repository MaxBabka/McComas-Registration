from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import date
from selenium.webdriver.chrome.options import Options
import time
import datetime

options = Options()

day1 = datetime.date.today()
print(day1)
day2 = datetime.date.today() + datetime.timedelta(days=1)
day3 = datetime.date.today() + datetime.timedelta(days=2)
day4 = datetime.date.today() + datetime.timedelta(days=3)
givenDate = input('Please enter a date that you would like to reserve')
currentDate = datetime.datetime.strptime('01/08/2015','%d/%m/%Y').date()

#Goes to recsports website
DRIVER_PATH = './chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://connect.recsports.vt.edu/booking/d71f0446-5a7b-4dee-9549-9f6f3add4812')

login = open(r'Login.txt')
today = date.today()
try:
    # login user
    pidButton = driver.find_element_by_xpath("//button[@title='VT PID']").click()  # Click the login button
    USERNAME = login.readline()
    PASSWORD = login.readline()
    DUO_CODE = login.readline()
    USERNAME = USERNAME.strip('\n')
    PASSWORD = PASSWORD.strip('\n')
    DUO_CODE = DUO_CODE.strip('\n')

    vtUsername = driver.find_element_by_xpath("//input[@id='username']").send_keys(USERNAME)
    vtPassword = driver.find_element_by_xpath("//input[@id='password']").send_keys(PASSWORD)
    vtLogin = driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()

    # Code here is after you have logged in and are trying to authenticate using Duo Mobile
    driver.switch_to.frame("duo_iframe")
    try:
        time.sleep(4)
        cancelPush = driver.find_element_by_xpath("//button[@class='btn-cancel']").click()
    except NoSuchElementException:
        print("No cancel button was found!")

    # These two try catch blocks should try to press the enter a passcode button
    try:
        time.sleep(3)
        driver.find_element_by_xpath("//button[@class='positive auth-button' and contains(.,'Enter a Passcode ')]") \
            .click()
    except NoSuchElementException:
        driver.find_element_by_xpath("//button[@class='auth-button positive' and contains(.,'Enter a Passcode ')]") \
            .click()
        print("positive auth not found!")

    duoCode = driver.find_element_by_xpath("//input[@type='text']").send_keys(DUO_CODE)
    driver.find_element_by_xpath("//button[@type='submit' and contains(.,'Log In')]").click()

except NoSuchElementException:
    print('Already logged in!')

# At this point you are inside of the McComas's website
driver.switch_to.default_content
# dates = driver.find_element_by_xpath("//h3[@class='text-primary']")
# print(dates)

# days = {'first day': [time, time, otherTime], 'second day': []}

# Find the days that you can register for so we can pull the timeslots
# def getDays:
    # days =

# Loop through each time slot calling the parseSlot method
# Use for loop
# def parseTimeSlots:


# Analyzes a time slot determining if it is available
# Return what time it is
# def parseSlot:

