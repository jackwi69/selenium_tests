import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

def test_init():
    driver: WebDriver = webdriver.Chrome()
    return driver


def test_select_options():
    driver = test_init()
    driver.get('https://selenium.dev/selenium/web/formPage.html')

    select_element = driver.find_element(By.NAME, 'selectomatic')
    select = Select(select_element)

    two_element = driver.find_element(By.CSS_SELECTOR, 'option[value=two]')
    four_element = driver.find_element(By.CSS_SELECTOR, 'option[value=four]')
    count_element = driver.find_element(By.CSS_SELECTOR, "option[value='still learning how to count, apparently']")

    select.select_by_visible_text('Four')
    assert four_element.is_selected()

    select.select_by_value('two')
    assert two_element.is_selected()

    select.select_by_index(3)
    assert count_element.is_selected()


def test_select_multiple_options():
    driver = test_init()
    driver.get('https://selenium.dev/selenium/web/formPage.html')
    select_element = driver.find_element(By.NAME, 'multi')
    select = Select(select_element)

    ham_element = driver.find_element(By.CSS_SELECTOR, 'option[value=ham]')
    gravy_element = driver.find_element(By.CSS_SELECTOR, "option[value='onion gravy']")
    egg_element = driver.find_element(By.CSS_SELECTOR, 'option[value=eggs]')
    sausage_element = driver.find_element(By.CSS_SELECTOR, "option[value='sausages']")

    option_elements = select_element.find_elements(By.TAG_NAME, 'option')
    option_list = select.options
    assert option_elements == option_list

    selected_option_list = select.all_selected_options
    expected_selection = [egg_element, sausage_element]
    assert selected_option_list == expected_selection

    select.select_by_value('ham')
    select.select_by_value('onion gravy')
    assert ham_element.is_selected()
    assert gravy_element.is_selected()

    select.deselect_by_value('eggs')
    select.deselect_by_value('sausages')
    assert not egg_element.is_selected()
    assert not sausage_element.is_selected()

def test_disabled_options():
    driver = test_init()
    driver.get('https://selenium.dev/selenium/web/formPage.html')

    select_element = driver.find_element(By.NAME, 'single_disabled')
    select = Select(select_element)

    with pytest.raises(NotImplementedError):
        select.select_by_value('disabled')

"""
/home/john/anaconda3/bin/python /snap/pycharm-community/383/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py --path /home/john/PycharmProjects/Selenium_test/test_select_list_01.py 
Testing started at 18:14 ...
Launching pytest with arguments /home/john/PycharmProjects/Selenium_test/test_select_list_01.py --no-header --no-summary -q in /home/john/PycharmProjects/Selenium_test

============================= test session starts ==============================
collecting ... collected 4 items

test_select_list_01.py::test_init PASSED                                 [ 25%]
test_select_list_01.py::test_select_options PASSED                       [ 50%]
test_select_list_01.py::test_select_multiple_options PASSED              [ 75%]
test_select_list_01.py::test_disabled_options PASSED                     [100%]

========================= 4 passed, 1 warning in 9.17s =========================

Process finished with exit code 0
"""