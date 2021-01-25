from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import date
DRIVER_PATH = './chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://connect.recsports.vt.edu/booking/d71f0446-5a7b-4dee-9549-9f6f3add4812')

today = date.today()
# try:
#     pidButton = driver.find_element_by_xpath("//button[@title='VT PID']").click() #Click the login button
#     vtUsername = driver.find_element_by_xpath("//input[@id='username']").send_keys(USERNAME)
#     vtPassword = driver.find_element_by_xpath("//input[@id='password']").send_keys(PASSWORD)
#     vtLogin = driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
# except NoSuchElementException:
#     print('Already logged in!')

dates = driver.find_element_by_xpath("//h3[@class='text-primary']")
print(dates)




