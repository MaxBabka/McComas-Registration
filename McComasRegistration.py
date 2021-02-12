from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import date
from selenium.webdriver.chrome.options import Options
import time
import datetime

# Attempts to use Chrome profile

day1 = datetime.date.today()
print(day1)
day2 = datetime.date.today() + datetime.timedelta(days=1)
day3 = datetime.date.today() + datetime.timedelta(days=2)
day4 = datetime.date.today() + datetime.timedelta(days=3)
givenDate = input('Please enter a date that you would like to reserve')
currentDate = datetime.datetime.strptime('01/08/2015','%d/%m/%Y').date()

options = Options()

#Goes to recsports website
DRIVER_PATH = './chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://connect.recsports.vt.edu/booking/d71f0446-5a7b-4dee-9549-9f6f3add4812')

today = date.today()
try:
    # login user
    pidButton = driver.find_element_by_xpath("//button[@title='VT PID']").click()  # Click the login button
    USERNAME = input('Username please')
    vtUsername = driver.find_element_by_xpath("//input[@id='username']").send_keys(USERNAME)
    PASSWORD = input('Password please')
    vtPassword = driver.find_element_by_xpath("//input[@id='password']").send_keys(PASSWORD)
    vtLogin = driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()

    # Code here is after you have logged in and are trying to authenticate using Duo Mobile
    driver.switch_to.frame("duo_iframe")
    try:
        time.sleep(4)
        driver.implicitly_wait(3)
        cancelPush = driver.find_element_by_xpath("//button[@class='btn-cancel']").click()
    except NoSuchElementException:
        print("No cancel button was found!")

    # These two try catch blocks should try to press the enter a passcode button
    try:
        time.sleep(3)
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("//button[@class='positive auth-button' and contains(.,'Enter a Passcode ')]") \
            .click()
    except NoSuchElementException:
        print("positive auth not found!")
    try:
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("//button[@class='auth-button positive' and contains(.,'Enter a Passcode ')]") \
            .click()
    except NoSuchElementException:
        print("auth positive not found!")
    CODE = input('Input Duo Code please!')
    duoCode = driver.find_element_by_xpath("//input[@type='text']").send_keys(CODE)
    driver.find_element_by_xpath("//button[@type='submit' and contains(.,'Log In')]").click()

except NoSuchElementException:
    print('Already logged in!')
print("MADE IT TO HERE")

# At this point you are inside of the McComas's website
# days = {'first day': [time, time, otherTime], 'second day': []}

# Find the days that are available for registration
# day1 = datetime.date(datetime.now())
# day2 =
# day3 =
# day4 =
# if day given by user is the same as an available day, click on that day
# Loop through each time slot calling the parseSlot method
# Use for loop
# def parseTimeSlots:


# Analyzes a time slot determining if it is available
# Return what time it is
# def parseSlot:
