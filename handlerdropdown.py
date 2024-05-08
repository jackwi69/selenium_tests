from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.select.html
# from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
import time

""" Session-7 """

# https://pypi.org/project/webdriver-manager/
# ### install: webdriver-manager 4.0.1 ### pip install webdriver-manager
# driver = webdriver.Chrome(service=ChromiumService(
#     ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

driver = webdriver.Chrome()

driver.get("https://www.opencart.com/index.php?route=account/register")

# country = driver.find_elements(By.XPATH, "//select[@id='input-country']")
# country = driver.find_elements(By.XPATH, "//select[@name='country_id']")
country = Select(driver.find_elements(By.XPATH, "//select[@id='input-country']"))
# print(len(country))

# select = Select(driver.find_elements(By.XPATH, "//select[@id='input-country']"))

