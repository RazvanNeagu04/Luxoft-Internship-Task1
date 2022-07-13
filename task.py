import select
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

session = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
session.get(url="https://www.luxoft.com")

session.maximize_window()
time.sleep(3)

#button = WebDriverWait(session, 10).until(ec.element_to_be_clickable((By.XPATH, "//a[text()='CAREERS']")))

button = session.find_element(by=By.LINK_TEXT,value="CAREERS")
button.click()

time.sleep(3)

button = session.find_element(by = By.CLASS_NAME, value = "career-banner-button")
button.click()

time.sleep(5)

button = session.find_element(by = By.XPATH, value = "//select[@id= 'search_countries']/..")
button.click()
#button = Select(session.find_element(by = By.NAME, value = "countryID[]" ))
#button = Select(session.find_element(by = By.XPATH, value = "//span[contains(@aria-owns, 'search_countries')]//input"))
#button.select_by_visible_text()
countries = session.find_element(by = By.XPATH, value = "//span[contains(@aria-owns, 'search_countries')]//input")
countries.send_keys("RO")
countries.send_keys(Keys.ENTER)
time.sleep(5)








time.sleep(5)

