from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
import time


""" t-5 """

# https://pypi.org/project/webdriver-manager/
# ### install: webdriver-manager 4.0.1 ### pip install webdriver-manager
driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
# driver.implicitly_wait(10)

webDrrWt = WebDriverWait(driver, 10,
                         ignored_exceptions=[NoSuchElementException,
                                             ElementNotVisibleException,
                                             ElementNotSelectableException,
                                             Exception]
                         )

# input - email
# ver 1
""" """
searchlink = webDrrWt.until(EC.presence_of_element_located((By.XPATH, "//input[@id='Email']")))
searchlink.clear()
searchlink.send_keys("test@google.com")


# ver 2
email_box = driver.find_element(By.XPATH, "//input[@id='Email']")
email_box.clear()
email_box.send_keys("test@google.com")


print("result of text:", email_box.text) # empty
print("result of getAttribute:", email_box.get_attribute('value'))


# input - password
passwd = driver.find_element(By.XPATH, "//input[@id='Password']")
passwd.clear()
passwd.send_keys("abc")
print('passwd:', passwd.get_attribute('value')) # abc


# button - LOG IN
submit = driver.find_element(By.XPATH, "//button[@type='submit']")
print(submit.text) # LOG IN


print("result of getAttribute class:", submit.get_attribute('class')) # button-1 login-button
print("result of getAttribute name:", submit.get_attribute('name')) # none
print("result of getAttribute type:", submit.get_attribute('type')) # submit

# time.sleep(1)


driver.close()