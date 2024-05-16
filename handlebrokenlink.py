import requests
from selenium import webdriver
from selenium.common import (NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, \
    TimeoutException)
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
import time


""" Session-7 """

# https://pypi.org/project/webdriver-manager/
# ### install: webdriver-manager 4.0.1 ### pip install webdriver-manager
driver = webdriver.Chrome(service=ChromiumService(
    ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

webDrrWt = WebDriverWait(driver, 10, poll_frequency=2,
                         ignored_exceptions=[NoSuchElementException,
                                             ElementNotVisibleException,
                                             ElementNotSelectableException,
                                             TimeoutException,
                                             Exception]
                         )
driver.get("http://www.deadlinkcity.com/")

badlinks = driver.find_elements(By.TAG_NAME,"a")
count=0

for link in badlinks:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None

    if res.status_code>=400:
        print(url , ' is broken link')
        count += 1
    else:
        print(url, ' is valid link')

print('total number broken of links: ', count)
driver.close()