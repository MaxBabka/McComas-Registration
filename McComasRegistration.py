from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

DRIVER_PATH = './chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://connect.recsports.vt.edu/Account/Login')

try:
    pidButton = driver.find_element_by_xpath("//button[@title='VT PID']").click() #Click the login button
    vtUsername = driver.find_element_by_xpath("//input[@id='username']").send_keys()
    vtPassword = driver.find_element_by_xpath("//input[@id='password']").send_keys()
    vtLogin = driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
except NoSuchElementException:
    print('Already logged in!')



