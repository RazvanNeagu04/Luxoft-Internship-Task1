import select
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.binary_location = "C://Program Files//Google//Chrome Beta//Application//chrome.exe"

session = webdriver.Chrome(service=Service(ChromeDriverManager('104.0.5112.20').install()), options=chrome_options)
session.get(url="https://www.luxoft.com")

session.maximize_window()
time.sleep(3)

#button = WebDriverWait(session, 10).until(ec.element_to_be_clickable((By.XPATH, "//a[text()='CAREERS']")))

button = session.find_element(by=By.LINK_TEXT,value="CAREERS")
button.click()

time.sleep(3)

button = session.find_element(by = By.CLASS_NAME, value = "career-banner-button")
button.click()

time.sleep(2)
session.execute_script("window.scrollTo(0, 1000)")
time.sleep(3)



button = session.find_element(by = By.XPATH, value = "//select[@id= 'search_countries']/..")
button.click()
countries = session.find_element(by = By.XPATH, value = "//span[contains(@aria-owns, 'search_countries')]//input")
countries.send_keys("RO")
countries.send_keys(Keys.ENTER)

time.sleep(3)

button = session.find_element(by = By.XPATH, value = "//select[@id='search_cities']/..")
button.click()
city = session.find_element(by = By.XPATH, value = "//span[contains(@aria-owns, 'search_cities')]//input")
city.send_keys("BU")
city.send_keys(Keys.ENTER)

time.sleep(3)

button = session.find_element(by = By.XPATH, value = "//select[@id='search_type']/..")
button.click()
specialization = session.find_element(by = By.XPATH, value = "//span[contains(@aria-owns, 'search_type')]//input")
specialization.send_keys("QA")
specialization.send_keys(Keys.ENTER)

time.sleep(2)

button = session.find_element(by = By.ID, value = "save-country-ids")
button.click()

time.sleep(3)

number_of_Offers_page1 = session.find_elements(by = By.XPATH, value = "//tr[contains(@data-offers-id,'')]")
session.execute_script("window.scrollTo(0, 1250)")
time.sleep(2)
button = session.find_element(by= By.ID, value= "previous_page")
button.click()
time.sleep(2)
number_of_Offers_page2 = session.find_elements(by = By.XPATH, value = "//tr[contains(@data-offers-id,'')]")
print(len(number_of_Offers_page1) + len(number_of_Offers_page2) - 2)

time.sleep(5)

