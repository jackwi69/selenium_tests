from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
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
                                             Exception]
                         )
driver.get("https://testautomationpractice.blogspot.com/")

# one element checkbox
# search_link = webDrrWt.until(EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")))
# search_link.click()

# all elements checkbox
search_links = webDrrWt.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")))
print(len(search_links))    # 7

# clikcked all checkbox
for x in range(len(search_links)):
    print(search_links[x].click())


time.sleep(1)
print("if weekname == monday or weekname == sunday\n")
for x in search_links:
    weekname = x.get_attribute('id')
    if weekname == 'monday' or weekname == 'sunday':
        x.click()   # uncheck


""" last to checkboxes unclick """
for z in range(len(search_links)-2, len(search_links)):
    search_links[z].click()

""" firs two elements checkbox """
# for x in range(len(search_links)):
#     if x<2:
#         search_links[x].click()

""" if selected """
# for x in search_links:
#     if x.is_selected():
#         x.click()

time.sleep(1)
for x in search_links:
    print('type: ', x.tag_name,', selected: ', x.is_selected())  # clikcked all


# you have to use find_elements !
# checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
# print(len(checkboxes)) # TypeError: object of type 'WebElement' has no len()
# print(len(checkboxes)) # 7
# for x in range(len(checkboxes)):
#     print(checkboxes[x].click())  # clikcked all

time.sleep(2)
driver.close()