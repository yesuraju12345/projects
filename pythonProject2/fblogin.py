
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome("C:\\Users\\hp\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.google.com/")
time.sleep(8)
driver.get("https://www.facebook.com/")

time.sleep(8)
driver.find_element(By.ID,"firstname").send_keys("kranthi")
driver.find_element(By.ID,"lastname").send_keys("hi")
driver.find_element(By.NAME,"u_0_g_9S").send_keys(970395112)
time.sleep(8)




