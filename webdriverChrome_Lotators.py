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

# task to do 1
""" no results """

# Navigate to the url
# driver.get('https://pythonexamples.org/tmp/selenium/index-19.html')

# Get the div element you are interested in
# mydiv = driver.find_element(By.ID, 'parent')
# time.sleep(1)

# Get children of mydiv
# children = mydiv.find_elements(By.XPATH, '*')
# time.sleep(1)

# Itertae over the children
# for child in children:
#     print("\nChild Element")
#     print(child.get_attribute('outerHTML'))

#####################################################

# task to do 2

# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# time.sleep(1)

""" error if dont install !!
driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
then LINK_TEXT will by error !
"""
# ### founded
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "OrangeHRM").click()
# driver.find_element(By.XPATH, '//a[text()="OrangeHRM, Inc"]').click()
# driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a").click()
# driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/p[2]/a[1]").click()
# driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']").click()
# driver.find_element(By.CSS_SELECTOR,"a[href='http://www.orangehrm.com']").click()
# driver.find_element(By.XPATH, "//a[text()='OrangeHRM, Inc']").click()

# ### error !!!
# driver.find_element(By.XPATH, "//a[contains(text(), 'OrangeHRM, Inc']").click()
time.sleep(3)

driver.close()