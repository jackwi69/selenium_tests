from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
# weit
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# v02
from selenium.webdriver.common.action_chains import ActionChains

# https://pypi.org/project/webdriver-manager/
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#############################################
## ver 01
driver.get("https://jqueryui.com/datepicker/")
time.sleep(1)
# driver.find_element(By.XPATH, "//iframe[@class='demo-frame']").click()
clicked = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
clicked.click()

time.sleep(1)

#############################################
# ver 02
# import ActionChains - NoSuchElementException
# action_chain = ActionChains(driver)
# hover = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
# action_chain.move_to_element(hover).perform()      # hover to show drop down list

driver.close()