from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
import time


""" t-6 """

# https://pypi.org/project/webdriver-manager/
# ### install: webdriver-manager 4.0.1 ### pip install webdriver-manager
driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

webDrrWt = WebDriverWait(driver, 10,
                         ignored_exceptions=[NoSuchElementException,
                                             ElementNotVisibleException,
                                             ElementNotSelectableException,
                                             Exception]
                         )

driver.get("https://google.com")
time.sleep(3)

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys("Selenium")
search_box.submit()

# Ok, must bi added 1 tuples mor: element_located((By. ...)))
# search_link = webDrrWt.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
# Ok, must bi added 1 tuples mor: element_located((By. ...)))
search_link = webDrrWt.until(EC.presence_of_element_located((By.XPATH, "//h3[normalize-space()='Selenium']")))
search_link.click()

driver.close()