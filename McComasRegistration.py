from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import date
from selenium.webdriver.chrome.options import Options
import time
import datetime

options = Options()

# Goes to recsports website
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

    # enters user's credentials to login
    vtUsername = driver.find_element_by_xpath("//input[@id='username']").send_keys(USERNAME)
    vtPassword = driver.find_element_by_xpath("//input[@id='password']").send_keys(PASSWORD)
    vtLogin = driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()

    # Code here is after you have logged in and are trying to authenticate using Duo Mobile
    driver.switch_to.frame("duo_iframe")
    try:
        time.sleep(3)
        cancelPush = driver.find_element_by_xpath("//button[@class='btn-cancel']").click()
    except NoSuchElementException:
        print("No cancel button was found!")

    # These two try catch blocks should try to press the enter a passcode button
    if len(DUO_CODE) == 0:
        time.sleep(2)
        driver.find_element_by_xpath("//button[@class='positive auth-button' and contains(.,'Call Me ')]").click()
    else:
        try:
            time.sleep(1)
            driver.find_element_by_xpath("//button[@class='positive auth-button' and contains(.,'Enter a Passcode ')]") \
                .click()
            duoCode = driver.find_element_by_xpath("//input[@type='text']").send_keys(DUO_CODE)
            driver.find_element_by_xpath("//button[@type='submit' and contains(.,'Log In')]").click()
        except NoSuchElementException:
            driver.find_element_by_xpath("//button[@class='auth-button positive' and contains(.,'Enter a Passcode ')]") \
                .click()
            duoCode = driver.find_element_by_xpath("//input[@type='text']").send_keys(DUO_CODE)
            driver.find_element_by_xpath("//button[@type='submit' and contains(.,'Log In')]").click()
            print("positive auth not found!")

except NoSuchElementException:
    print('Already logged in!')

# At this point you are inside of the McComas's website
# days = {'first day': [time, time, otherTime], 'second day': []}

# Find the days that are available for registration
# day1 = datetime.date.today()
# day2 = datetime.date.today() + datetime.timedelta(days=1)
# day3 = datetime.date.today() + datetime.timedelta(days=2)
# day4 = datetime.date.today() + datetime.timedelta(days=3)
# givenDate = input('Please enter the date on which you would like to reserve \nin the format year-month-day')
# currentDate = datetime.datetime.strptime('01/08/2015', '%d/%m/%Y').date()
# print(currentDate)
# # if day given by user is the same as an available day, click on that day
# if day1 == givenDate:
#     day1Button = driver.find_element_by_xpath("//button[@data-button-index='1']").click()
# elif day2 == givenDate:
#     day1Button = driver.find_element_by_xpath("//button[@data-button-index='1']").click()
# elif day3 == givenDate:
#     day1Button = driver.find_element_by_xpath("//button[@data-button-index='1']").click()
# elif day4 == givenDate:
#     day1Button = driver.find_element_by_xpath("//button[@data-button-index='1']").click()
# else:
#     print('Please Enter A Valid Day In The Format: year-month-day')


# Loop through each time slot calling the parseSlot method
# Use for loop
# def parseTimeSlots:


# Analyzes a time slot determining if it is available
# Return what time it is
# def parseSlot:
