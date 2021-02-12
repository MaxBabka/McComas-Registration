from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import date
from selenium.webdriver.chrome.options import Options
import time

# Attempts to use Chrome profile
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_argument(r'C:\Users\maxba\AppData\Local\Google\Chrome\User_Data\Default')

#Goes to recsports website
DRIVER_PATH = './chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://connect.recsports.vt.edu/booking/d71f0446-5a7b-4dee-9549-9f6f3add4812')

login = open(r'Login.txt')
today = date.today()
try:
    # login user
    pidButton = driver.find_element_by_xpath("//button[@title='VT PID']").click()  # Click the login button
    print("CLicked the login button")
    USERNAME = login.readline()
    PASSWORD = login.readline()
    DUO_CODE = login.readline()
    print(USERNAME)
    print("About to sleep!")
    time.sleep(3)
    print("Finished sleeping!")
    vtUsername = driver.find_element_by_xpath("//input[@id='username']").send_keys(USERNAME)
    print("About to sleep!")
    time.sleep(3)
    print("Finished sleeping!")
    vtPassword = driver.find_element_by_xpath("//input[@id='password']").send_keys(PASSWORD)
    # vtLogin = driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()

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
        print("positive auth not found!")
    try:
        driver.find_element_by_xpath("//button[@class='auth-button positive' and contains(.,'Enter a Passcode ')]") \
            .click()
    except NoSuchElementException:
        print("auth positive not found!")

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

