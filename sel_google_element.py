import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get('http://google.pl')
# time.sleep(1)
""" ver 1, Automation Step by Step"""
# googleSearch = driver.find_element(By.ID,"APjFqb")
# googleSearch.send_keys('Servo Motor')
# googleSearch.send_keys((Keys.RETURN))

""" ver 2 """
# driver.find_element(By.ID,"APjFqb").send_keys('Servo Motor')
# time.sleep(1)
# driver.find_element(By.NAME,"btnK").click()
# ctrl + / (komments or uncomments)

time.sleep(1)
driver.get("https://trytestingthis.netlify.app/index.html")
driver.find_element(By.NAME, "fname").send_keys('Jack')
driver.find_element(By.NAME, "lname").send_keys('Wi')
time.sleep(1)
# driver.implicitly_wait(2)

# driver.find_element(By.CLASS_NAME,"btn-success").click()
""" absolute path """
# driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/div[2]/form[1]/fieldset[1]/button[1]")
""" absolute path """
driver.find_element(By.XPATH,"//button[@class='btn btn-success']")
time.sleep(1)
# driver.implicitly_wait(2)

driver.close()