from selenium import webdriver

DRIVER_PATH = './chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://connect.recsports.vt.edu/Account/Login')

pidButton = driver.find_element_by_xpath("//button[@title='VT PID'").click()
