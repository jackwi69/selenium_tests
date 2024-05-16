from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
import time

# https://pypi.org/project/webdriver-manager/
# ### install: webdriver-manager 4.0.1 ### pip install webdriver-manager
driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

driver.get('https://demo.nopcommerce.com/')
time.sleep(1)
""" single elemet """
element = driver.find_element(By.XPATH,"//div[@class='footer']//a")
print(element.text + '\n') # Sitemap
time.sleep(1)

""" many elemets """
elements = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
for x in elements:
    print(x.text)

driver.close()
"""
Sitemap

Sitemap
Shipping & returns
Privacy notice
Conditions of Use
About us
Contact us
Search
News
Blog
Recently viewed products
Compare products list
New products
My account
Orders
Addresses
Shopping cart
Wishlist
Apply for vendor account
Facebook
Twitter
RSS
YouTube
nopCommerce
"""