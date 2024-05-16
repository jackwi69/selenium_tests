from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
import time

""" Session-7 """

driver = webdriver.Chrome(service=ChromiumService(
    ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

# driver = webdriver.Chrome()

""" select = Select(country)
             ^^^^^^^^^^^^^^^
  File "/home/john/anaconda3/lib/python3.11/site-packages/selenium/webdriver/support/select.py", line 38, in __init__
    if webelement.tag_name.lower() != "select":
       ^^^^^^^^^^^^^^^^^^^
  AttributeError: 'list' object has no attribute 'tag_name'
"""
#                           ERROR !!!

# driver.get("https://www.opencart.com/index.php?route=account/register")
# country = driver.find_elements(By.XPATH,"//select[@id='input-country']")
# country = driver.find_elements(By.CSS_SELECTOR,"select[@id='input-country']")
# country = driver.find_elements(By.CSS_SELECTOR,"#input-country")
# select = Select(country)
# select.select_by_visible_text("Poland")

#######################################

""" working - OK """

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
# elements = driver.find_elements(By.XPATH,"//select[@name='my-select']")
# ok
elements = driver.find_element(By.CSS_SELECTOR, "select[name='my-select']")
select = Select(elements)

print(dir(select))
""" ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', 
'__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', 
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__', '__weakref__', '_el', '_escape_string', 
'_get_longest_token', '_set_selected', '_unset_selected', 'all_selected_options', 
'deselect_all', 'deselect_by_index', 'deselect_by_value', 'deselect_by_visible_text', 
'first_selected_option', 'is_multiple', 'options', 'select_by_index', 'select_by_value', 
'select_by_visible_text']
"""
one = select.select_by_index(0)
select.select_by_visible_text('One')
time.sleep(2)
select.select_by_visible_text('Two')
time.sleep(2)
select.select_by_index(3) # Three
time.sleep(2)

# v02

# elements = driver.find_element(By.CSS_SELECTOR, "select[name='my-select']")
select2 = Select(driver.find_element(By.CSS_SELECTOR, "select[name='my-select']"))
select2.select_by_visible_text("One")
time.sleep(2)

driver.close()
