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
driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()

# one element checkbox
# search_link = webDrrWt.until(EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")))
# search_link.click()

# all elements checkbox
# search_links = webDrrWt.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")))
# print(len(search_links))    # 7

# time.sleep(1)
"""  Link & Xpath - Ok """
# search_link = webDrrWt.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='top-menu notmobile']//a[normalize-space()='Digital downloads']")))
# search_link.click()
# driver.find_element(By.LINK_TEXT, "Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()
# driver.find_element(By.XPATH, "//ul[@class='top-menu notmobile']//a[normalize-space()='Digital downloads']").click()

""" find number of links od page """
links2 = driver.find_elements(By.XPATH, "//a")
print('totlal numebr of links: ', len(links2)) # 87

links1 = driver.find_elements(By.TAG_NAME, "a")
print('totlal numebr of links: ', len(links1)) # 87




time.sleep(2)
driver.close()