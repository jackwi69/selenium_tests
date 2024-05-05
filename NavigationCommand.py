""" v01 """
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
import time

# https://pypi.org/project/webdriver-manager/
# ### install: webdriver-manager 4.0.1 ### pip install webdriver-manager
driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

driver.get("https://snapdeal.com")
time.sleep(2)
driver.get("https://amazon.com")
time.sleep(1)

driver.back()
time.sleep(1)

driver.forward()
driver.refresh()

driver.close()