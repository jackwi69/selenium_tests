from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(20)
driver.get('https://www.amazon.com/')
print('driver.title: ', driver.title) # driver.title: Amazon.com

driver.implicitly_wait(20)
""" input search """
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('T-shert')
""" press button """
driver.find_element(By.ID, 'nav-search-submit-text').click()

driver.implicitly_wait(20)
driver.get('https://www.amazon.com/Alienware-Low-Profile-RGB-Gaming-Keyboard/dp/B07V8MXJB1?ref_=Oct_DLandingS_D_7af4cef2_0&th=1')

driver.implicitly_wait(20)
#driver.find_element(By.CLASS_NAME, 'product-title-word-break').click()
spams = driver.find_element(By.ID, 'add-to-cart-button').click()
# driver.title:  Amazon.com Shopping Cart

driver.implicitly_wait(2)
driver.find_element(By.NAME,'proceedToRetailCheckout').click()

driver.implicitly_wait(2)
driver.find_element(By.ID,'ap_email').send_keys('abc#google.com')
driver.find_element(By.ID,'continue').click() # driver.title:  Amazon Sign-In

driver.implicitly_wait(200)
print('driver.title: ', driver.title) 
# driver.title:  Amazon.com: Alienware Low-Profile RGB Gaming Keyboard AW510K: Alienfx Per Key RGB LED - Media CONTROLS & USB Passthrough - Cherry MX Low Profile Red Switches : Electronics

driver.close()