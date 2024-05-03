import time
from selenium import webdriver
from selenium.common import NoSuchElementException
#from selenium.webdriver import Keys
#from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

""" Session 2- Selenium with Python """
#https://www.youtube.com/watch?v=4DHefIyw6ik&list=PLUDwpEzHYYLsuUBvuoYTlN0KsBB5t-BDa&index=2

driver = webdriver.Chrome()
# driver.get('https://demo.nopcommerce.com/')
# time.sleep(1)

""" search """
# driver.find_element(By.ID, 'small-searchterms').send_keys('Lenovo Thinkpad X1 Carbon Laptop')
# driver.find_element(By.NAME, 'q').send_keys('Lenovo Thinkpad X1 Carbon Laptop')
# time.sleep(1)
""" button """
# driver.find_element(By.CLASS_NAME, "search-box-button").click()
# driver.find_element(By.XPATH,"//button[@type='submit']")

""" LINK_TEXT """
# driver.find_element(By.XPATH,"//a[@class='ico-register']").click()
# driver.find_element(By.CLASS_NAME, "ico-register").click()

""" link OK! """
# links = driver.find_element(By.TAG_NAME,"a")
# print(type(links)) # list
# print(len(str(links))) # 180, # 11118



try:
    # driver.get("https://www.geeksforgeeks.org/")
    """ LINK_TEXT & PARTIAL_LINK_TEXT - error ? """
    # driver.find_element(By.LINK_TEXT,"Tutorials").click()
    # driver.find_element(By.CSS_SELECTOR, "//a[normalize-space()='Register']").click()
    # time.sleep(2)
    # driver.find_element(By.PARTIAL_LINK_TEXT,"Regi").click()

    ###################################################
    # driver.get("http://www.automationpractice.pl/index.php")
    # time.sleep(1)

    """ TAG_NAME """
    # sliders = driver.find_elements(By.TAG_NAME,"//div[@id='homepage-slider']")
    # print(len(str(sliders)))
    # time.sleep(1)

    # sliders = driver.find_elements(By.TAG_NAME, "a")
    # print(len(sliders)) # 88

    ###################################################
    driver.get("https://www.facebook.com/")
    # driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
    # driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc")
    # class="inputtext _55r1 _6luy" # 3 klasy


    """ OK - CLASS_NAME """
    # driver.find_element(By.CLASS_NAME, "inputtext").send_keys("abc@google.com")

    """ error - CSS_SELECTOR, add dot.  """
    # driver.find_element(By.CSS_SELECTOR, "inputtext").send_keys("abc@google.com")

    """ CSS_SELECTOR - OK! """
    # driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abc@google.com")
    # driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("abc@google.com")

    """ tag & attribute, OK! """
    # driver.find_element(By.CSS_SELECTOR,'input[data-testid=royal_email]').send_keys("abc@google.com")
    # driver.find_element(By.CSS_SELECTOR, '[data-testid=royal_email]').send_keys("abc@google.com")

    """ must by bracket [..] """
    # driver.find_element(By.CSS_SELECTOR, 'data-testid=royal_email').send_keys("abc@google.com")

    """ tag, class & attribute """
    """ <input type="password" class="inputtext _55r1 _6luy _9npi" name="pass" id="pass" data-testid="royal_pass" """
    driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_email]").send_keys("acb@google.com")
    driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass]").send_keys("pass")

    time.sleep(1)

except NoSuchElementException as e:
    print(e)

time.sleep(1)

driver.close()