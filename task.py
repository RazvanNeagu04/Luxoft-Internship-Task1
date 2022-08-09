import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from Home_Page import Home_Page
from baseclass import Base

chrome_options = Options()
chrome_options.binary_location = "C://Program Files//Google//Chrome Beta//Application//chrome.exe"


#session_instance = webdriver.Chrome(service=Service(ChromeDriverManager('104.0.5112.20').install()), options=chrome_options)
#session =webdriver.Chrome(service=Service(ChromeDriverManager().install()))
session_instance= Base()
session_instance.navigate_to("https://www.luxoft.com")
session_instance.maximize()
time.sleep (5)

button = session_instance.find_element_by_link_text(element="CAREERS")
if button:
    button.click()
else:
    print("button was not found")
    sys.exit(1)


time.sleep(5)

button = session_instance.find_element_by_link_text(element="SEARCH JOBS")
button.click()
time.sleep(5)


button = session_instance.find_element_by_xpath(element ="//span[contains(text(),'Countries')]/..")
coordinates = button.location_once_scrolled_into_view
time.sleep(2)
session_instance.scroll_to_value()
button.click()
countries = session_instance.find_element_by_xpath(element ="//span[contains(@aria-owns, 'search_countries')]//input")
countries.send_keys("RO")
countries.send_keys(Keys.ENTER)
time.sleep(5)


button = session_instance.find_element_by_xpath(element ="//span[contains(text(),'Cities')]/..")
#coordinates = button.location_once_scrolled_into_view
#time.sleep(2)
#session_instance.scroll_to_value()
button.click()
cities = session_instance.find_element_by_xpath(element ="//span[contains(@aria-owns, 'search_cities')]//input")
cities.send_keys("Bucharest")
cities.send_keys(Keys.ENTER)
time.sleep(5)


#button = session_instance.find_element(by = By.XPATH, value ="//span[contains(text(),'Specializations')]/..")
button = session_instance.find_element_by_xpath(element="//span[contains(text(),'Specializations')]/..")
#coordinates = button.location_once_scrolled_into_view
#time.sleep(2)
#session_instance.execute_script(f"window.scrollTo({coordinates['x']}, {coordinates['y'] - 300})")
button.click()
specializations = session_instance.find_element_by_xpath(element ="//span[contains(@aria-owns, 'search_type')]//input")
#specializations = session.find_element(by = By.CLASS_NAME, value = "form-group form-group-select form-group-select-specialization")
specializations.send_keys("QA automation")
specializations.send_keys(Keys.ENTER)
time.sleep(5)


#button = session.find_element(by = By.CLASS_NAME, value = "career-jobs__btn")
#button = session.find_element(by=By.CLASS_NAME,value="career-jobs__btn carrer-btn-orange")
#button = session.find_element(by=By.ID,value="save-country-ids")
#button = WebDriverWait(session, 3).until(ec.element_to_be_clickable((By.ID,"save-country-ids")))
button = session_instance.find_element_by_id(element ="save-country-ids")
button.click()
time.sleep(5)



number_of_Offers_page1 = session_instance.find_elements_by_xpath(element ="//tr[contains(@data-offers-id,'')]")
session_instance.scroll_to_value()
time.sleep(2)
button = session_instance.find_element_by_id(element="previous_page")
button.click()
time.sleep(2)
number_of_Offers_page2 = session_instance.find_elements_by_xpath(element ="//tr[contains(@data-offers-id,'')]")
print(number_of_Offers_page1)
print(len(number_of_Offers_page1) + len(number_of_Offers_page2) - 2)

time.sleep(5)











# "//button[contains(@class,'career-jobs')]"
# "//button[@id = 'save-country-ids']"
# //button[text()='Search']


session_itself = session_instance.session
homepage_instance = Home_Page(session=session_itself)
if not homepage_instance.navigate_to_careers():
    print("ERROR - Home Page navigation to Crareers failed. Stopping test")
    sys.exit(1)
