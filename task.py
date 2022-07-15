import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

session =webdriver.Chrome(service=Service(ChromeDriverManager().install()))
session.get(url="https://www.luxoft.com")
session.maximize_window()
time.sleep (5)

button = session.find_element(by=By.LINK_TEXT,value="CAREERS")
button.click()
time.sleep(5)

button = session.find_element(by=By.LINK_TEXT,value="SEARCH JOBS")
button.click()
time.sleep(5)

#button = session.find_element(by = By.XPATH, value = "//select[@id= 'search_countries']/..")
button = session.find_element(by = By.XPATH, value = "//span[contains(text(),'Countries')]/..")
coordinates = button.location_once_scrolled_into_view
time.sleep(2)
session.execute_script(f"window.scrollTo({coordinates['x']}, {coordinates['y'] -300})")

button.click()

countries = session.find_element(by = By.XPATH, value = "//span[contains(@aria-owns, 'search_countries')]//input")
countries.send_keys("RO")

countries.send_keys(Keys.ENTER)

time.sleep(5)

# "//button[contains(@class,'career-jobs')]"
# "//button[@id = 'save-country-ids']"
# //button[text()='Search']