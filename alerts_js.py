from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome() # Ok
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()

# ("//button[@onclick='jsPrompt()']")
# ("//button[normalize-space()='Click for JS Prompt']")

driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(2)
alertwindow = driver.switch_to.alert
print(alertwindow.text) # I am a JS prompt
alertwindow.send_keys("weLcome")
alertwindow.accept()

driver.close()