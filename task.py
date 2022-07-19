import select
import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
chrome_options.binary_location = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe"


#from webdriver_manager.chrome import ChromeDriverManager

session = webdriver.Chrome(executable_path="C:\\Users\\alina\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe", options=chrome_options)
session.get(url="https://www.luxoft.com")

session.maximize_window()
time.sleep(2)

#button = WebDriverWait(session, 10).until(ec.element_to_be_clickable((By.XPATH, "//a[text()='CAREERS']")))

button = session.find_element(by=By.LINK_TEXT,value="CAREERS")
button.click()

time.sleep(2)

accept_button = session.find_element(by=By.XPATH, value="//a[contains(text(),'ACCEPT')]")
accept_button.click()


button = session.find_element(by = By.CLASS_NAME, value = "career-banner-button")
button.click()

time.sleep(5)


button = session.find_element(by = By.XPATH, value = "//select[@id= 'search_countries']/..")
coordinates = button.location_once_scrolled_into_view
time.sleep(2)
session.execute_script(f"window.scrollTo({coordinates['x']}, {coordinates['y'] -300})")
button.click()

#button = Select(session.find_element(by = By.NAME, value = "countryID[]" ))
#button = Select(session.find_element(by = By.XPATH, value = "//span[contains(@aria-owns, 'search_countries')]//input"))
#button.select_by_visible_text()

countries = session.find_element(by = By.XPATH, value = "//span[contains(@aria-owns, 'search_countries')]//input")
countries.send_keys("RO")
countries.send_keys(Keys.ENTER)
time.sleep(2)

button = session.find_element(by=By.XPATH, value="//div[@class='form-group form-group-select form-group-select-city']")
button.click()

cities = session.find_element(by=By.XPATH, value="//span[contains(@aria-owns, 'search_cities')]//input")
cities.send_keys("Bucharest")
cities.send_keys(Keys.ENTER)
time.sleep(2)



# specializations = session.find_element(by=By.XPATH, value ="//span[contains(@aria-owns, 'search_specializations')]//input")
# specializations.send_keys("QA automation")
# specializations.send_keys(Keys.ENTER)
# time.sleep(2)

button = session.find_element(by = By.XPATH, value = "//select[@id='search_type']/..")
button.click()
specialization = session.find_element(by = By.XPATH, value = "//span[contains(@aria-owns, 'search_type')]//input")
specialization.send_keys("QA")
specialization.send_keys(Keys.ENTER)

time.sleep(2)

button = session.find_element(by = By.ID, value = "save-country-ids")
button.click()

time.sleep(2)

offers_page1 = session.find_elements(by = By.XPATH, value = "//tr[contains(@data-offers-id,'')]")
session.execute_script("window.scrollTo(0, 1200)")

time.sleep(2)

button = session.find_element(by= By.ID, value= "previous_page")
button.click()

offers_page2 = session.find_elements(by = By.XPATH, value = "//tr[contains(@data-offers-id,'')]")
print("Nr de oferte  este:", len(offers_page1) + len(offers_page2) - 2)



time.sleep(2)
session.quit()
