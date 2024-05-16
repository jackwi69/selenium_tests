from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
time.sleep(0.5)


# conditional command - is_selected()
# is_displayed()
# is_enabled()
# is_selected()

searchBox = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("display status:", searchBox.is_displayed()) # True
print("Enabled status:", searchBox.is_enabled())   # True

# print(driver.find_element(By.XPATH, "//input[@id='small-searchterms']").is_displayed())
# print(driver.find_element(By.XPATH, "//input[@id='small-searchterms']").is_enabled())

driver.get("https://demo.nopcommerce.com/register")

print("\tbefore selecting button")
ro_bt_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
ro_bt_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")

print("male:", ro_bt_male.is_selected()) # False
print("male:", ro_bt_female.is_selected()) # False

# select radio male button
ro_bt_male.click()

print("\tAfter selecting button")
ro_bt_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
ro_bt_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")

print("male:", ro_bt_male.is_selected()) # true
print("male:", ro_bt_female.is_selected()) # false

# ###############################3

# driver.get("https://opensource-demo.orangehrmlive.com/")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# error
# driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
# driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a").click()
# driver.find_element(By.XPATH, "//a[contains(text(),'OrangeHRM, Inc']").click()
# driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()
# driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']")
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/p[2]/a[1]")

time.sleep(1)

driver.close()