import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


chrome_options = Options()
chrome_options.binary_location = "C://Program Files//Google//Chrome Beta//Application//chrome.exe"


session = webdriver.Chrome(service=Service(ChromeDriverManager('104.0.5112.20').install()), options=chrome_options)
#session =webdriver.Chrome(service=Service(ChromeDriverManager().install()))
session.get(url="https://www.luxoft.com")
session.maximize_window()
time.sleep (5)

button = session.find_element(by=By.LINK_TEXT,value="CAREERS")
button.click()
time.sleep(5)

button = session.find_element(by=By.LINK_TEXT,value="SEARCH JOBS")
button.click()
time.sleep(5)


button = session.find_element(by = By.XPATH, value = "//span[contains(text(),'Countries')]/..")
coordinates = button.location_once_scrolled_into_view
time.sleep(2)
session.execute_script(f"window.scrollTo({coordinates['x']}, {coordinates['y'] -300})")
button.click()
countries = session.find_element(by = By.XPATH, value = "//span[contains(@aria-owns, 'search_countries')]//input")
countries.send_keys("RO")
countries.send_keys(Keys.ENTER)
time.sleep(5)


button = session.find_element(by = By.XPATH, value = "//span[contains(text(),'Cities')]/..")
coordinates = button.location_once_scrolled_into_view
time.sleep(2)
session.execute_script(f"window.scrollTo({coordinates['x']}, {coordinates['y'] -300})")
button.click()
cities = session.find_element(by = By.XPATH, value = "//span[contains(@aria-owns, 'search_cities')]//input")
cities.send_keys("Bucharest")
cities.send_keys(Keys.ENTER)
time.sleep(5)


button = session.find_element(by = By.XPATH, value = "//span[contains(text(),'Specializations')]/..")
coordinates = button.location_once_scrolled_into_view
time.sleep(2)
session.execute_script(f"window.scrollTo({coordinates['x']}, {coordinates['y'] -300})")
button.click()
specializations = session.find_element(by = By.XPATH, value = "//span[contains(@aria-owns, 'search_type')]//input")
#specializations = session.find_element(by = By.CLASS_NAME, value = "form-group form-group-select form-group-select-specialization")
specializations.send_keys("QA automation")
specializations.send_keys(Keys.ENTER)
time.sleep(5)


#button = session.find_element(by = By.CLASS_NAME, value = "career-jobs__btn")
#button = session.find_element(by=By.CLASS_NAME,value="career-jobs__btn carrer-btn-orange")
#button = session.find_element(by=By.ID,value="save-country-ids")
#button = WebDriverWait(session, 3).until(ec.element_to_be_clickable((By.ID,"save-country-ids")))
button = session.find_element(by = By.ID, value = "save-country-ids")
button.click()
time.sleep(5)



number_of_Offers_page1 = session.find_elements(by = By.XPATH, value = "//tr[contains(@data-offers-id,'')]")
session.execute_script("window.scrollTo(0, 1250)")
time.sleep(2)
button = session.find_element(by= By.ID, value= "previous_page")
button.click()
time.sleep(2)
number_of_Offers_page2 = session.find_elements(by = By.XPATH, value = "//tr[contains(@data-offers-id,'')]")
print(len(number_of_Offers_page1) + len(number_of_Offers_page2) - 2)

time.sleep(5)









#da

# "//button[contains(@class,'career-jobs')]"
# "//button[@id = 'save-country-ids']"
# //button[text()='Search']