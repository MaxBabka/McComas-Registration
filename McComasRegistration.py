from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import date
from selenium.webdriver.chrome.options import Options

# Attempts to use Chrome profile
options = Options()
options.add_argument(r'C:\Users\maxba\AppData\Local\Google\Chrome\User_Data\Default')

#Goes to recsports website
DRIVER_PATH = './chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://connect.recsports.vt.edu/booking/d71f0446-5a7b-4dee-9549-9f6f3add4812')

today = date.today()
try:
    pidButton = driver.find_element_by_xpath("//button[@title='VT PID']").click()  # Click the login button
    USERNAME = input('Username please')
    vtUsername = driver.find_element_by_xpath("//input[@id='username']").send_keys(USERNAME)
    PASSWORD = input('Password please')
    vtPassword = driver.find_element_by_xpath("//input[@id='password']").send_keys(PASSWORD)
    vtLogin = driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
    # CODE = input('Input Duo Code please!')
    #click call button
    clickCallButton = driver.find_element_by_xpath("//button[@type='submit']").click()
    #duoCode = driver.find_element_by_xpath("//input[@type='text']").send_keys(CODE)
    #duoLogin = driver.find_element_by_xpath("//button[@tabindex='2']").click()


except NoSuchElementException:
    print('Already logged in!')
# print("MADE IT TO HERE")
# dates = driver.find_element_by_xpath("//h3[@class='text-primary']")
# print(dates)
