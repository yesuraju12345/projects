
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome("C:\\Users\\hp\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.google.com/")
time.sleep(8)
driver.get("https://www.facebook.com/")
time.sleep(8)
driver.find_element(By.ID,"email").send_keys("kranthimann123@gmail.com")
driver.find_element(By.ID,"pass").send_keys("Kr@nth123")
driver.find_element(By.NAME,"login").click()
time.sleep(8)




