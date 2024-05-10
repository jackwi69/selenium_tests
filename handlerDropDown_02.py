from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.os_manager import ChromeType
import time

from selenium.webdriver.support.wait import WebDriverWait

""" Session-7 """

driver: WebDriver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/#google_vignette")
driver.implicitly_wait(2)

# -------------------
# time.sleep(2)
# dropdown = driver.find_elements( by=By.XPATH, value="//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select")
# print(len(dropdown))
# print(type(dropdown))

# webDrrWt = WebDriverWait(driver, 10,
#                          ignored_exceptions=[NoSuchElementException,
#                                              ElementNotVisibleException,
#                                              ElementNotSelectableException,
#                                              Exception]
#                          )

# search_link = webDrrWt.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select")))

# time.sleep(2)
# country = driver.find_elements(By.XPATH, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select")
# print(len(country))
# select = Select(country)

# css "div[class='single_tab_div resp-tab-content resp-tab-content-active'] p select"

""" find_elements( ==> Error
select = Select(dropdown),  if webelement.tag_name.lower() != "select": AttributeError: 'list' object has no attribute 'tag_name'
# -------------------- 
    find_element( ==>  Ok !
driver.find_element(by=By.CSS_SELECTOR, value="div[class='single_tab_div resp-tab-content resp-tab-content-active'] p select")    
"""

# dropdown = driver.find_element(by=By.CSS_SELECTOR, value="div[class='single_tab_div resp-tab-content resp-tab-content-active'] p select")
# select = Select(dropdown)
# select.select_by_visible_text("Norway")
# time.sleep(1)
# select.select_by_index(1)

""" select = Select(driver.find_element(by=By.xxx """
select = Select(driver.find_element(by=By.CSS_SELECTOR, value="div[class='single_tab_div resp-tab-content resp-tab-content-active'] p select"))
select.select_by_visible_text("Peru")
time.sleep(1)
select.select_by_visible_text("Norway")
time.sleep(1)
select.select_by_index(1) # Aland Island
option_list = select.options
print(len(option_list)) # 249

for x in option_list:
    print(x.text)

time.sleep(2)

driver.close()

"""
Afghanistan
Åland Islands
Albania
Algeria
American Samoa
Andorra
Angola
Anguilla
Antarctica
Antigua and Barbuda
Argentina
Armenia
Aruba
Australia
Austria
Azerbaijan
Bahamas
Bahrain
Bangladesh
Barbados
Belarus
Belgium
Belize
Benin
Bermuda
Bhutan
Bolivia, Plurinational State of
Bonaire, Sint Eustatius and Saba
Bosnia and Herzegovina
Botswana
Bouvet Island
Brazil
British Indian Ocean Territory
Brunei Darussalam
Bulgaria
Burkina Faso
Burundi
Cambodia
Cameroon
Canada
Cape Verde
Cayman Islands
Central African Republic
Chad
Chile
China
Christmas Island
Cocos (Keeling) Islands
Colombia
Comoros
Congo
Congo, the Democratic Republic of the
Cook Islands
Costa Rica
Côte d’Ivoire
Croatia
Cuba
Curaçao
Cyprus
Czech Republic
Denmark
Djibouti
Dominica
Dominican Republic
Ecuador
Egypt
El Salvador
Equatorial Guinea
Eritrea
Estonia
Ethiopia
Falkland Islands (Malvinas)
Faroe Islands
Fiji
Finland
France
French Guiana
French Polynesia
French Southern Territories
Gabon
Gambia
Georgia
Germany
Ghana
Gibraltar
Greece
Greenland
Grenada
Guadeloupe
Guam
Guatemala
Guernsey
Guinea
Guinea-Bissau
Guyana
Haiti
Heard Island and McDonald Islands
Holy See (Vatican City State)
Honduras
Hong Kong
Hungary
Iceland
India
Indonesia
Iran, Islamic Republic of
Iraq
Ireland
Isle of Man
Israel
Italy
Jamaica
Japan
Jersey
Jordan
Kazakhstan
Kenya
Kiribati
Korea, Democratic People’s Republic of
Korea, Republic of
Kuwait
Kyrgyzstan
Lao People’s Democratic Republic
Latvia
Lebanon
Lesotho
Liberia
Libya
Liechtenstein
Lithuania
Luxembourg
Macao
Macedonia, the former Yugoslav Republic of
Madagascar
Malawi
Malaysia
Maldives
Mali
Malta
Marshall Islands
Martinique
Mauritania
Mauritius
Mayotte
Mexico
Micronesia, Federated States of
Moldova, Republic of
Monaco
Mongolia
Montenegro
Montserrat
Morocco
Mozambique
Myanmar
Namibia
Nauru
Nepal
Netherlands
New Caledonia
New Zealand
Nicaragua
Niger
Nigeria
Niue
Norfolk Island
Northern Mariana Islands
Norway
Oman
Pakistan
Palau
Palestinian Territory, Occupied
Panama
Papua New Guinea
Paraguay
Peru
Philippines
Pitcairn
Poland
Portugal
Puerto Rico
Qatar
Réunion
Romania
Russian Federation
Rwanda
Saint Barthélemy
Saint Helena, Ascension and Tristan da Cunha
Saint Kitts and Nevis
Saint Lucia
Saint Martin (French part)
Saint Pierre and Miquelon
Saint Vincent and the Grenadines
Samoa
San Marino
Sao Tome and Principe
Saudi Arabia
Senegal
Serbia
Seychelles
Sierra Leone
Singapore
Sint Maarten (Dutch part)
Slovakia
Slovenia
Solomon Islands
Somalia
South Africa
South Georgia and the South Sandwich Islands
South Sudan
Spain
Sri Lanka
Sudan
Suriname
Svalbard and Jan Mayen
Swaziland
Sweden
Switzerland
Syrian Arab Republic
Taiwan, Province of China
Tajikistan
Tanzania, United Republic of
Thailand
Timor-Leste
Togo
Tokelau
Tonga
Trinidad and Tobago
Tunisia
Turkey
Turkmenistan
Turks and Caicos Islands
Tuvalu
Uganda
Ukraine
United Arab Emirates
United Kingdom
United States
United States Minor Outlying Islands
Uruguay
Uzbekistan
Vanuatu
Venezuela, Bolivarian Republic of
Viet Nam
Virgin Islands, British
Virgin Islands, U.S.
Wallis and Futuna
Western Sahara
Yemen
Zambia
Zimbabwe
"""
