import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

session =webdriver.Chrome(service=Service(ChromeDriverManager().install()))
session.get(url="https://www.luxoft.com")
session.maximize_window()
time.sleep (5)

button = session.find_element(by=By.LINK_TEXT,value="CAREERS")
button.click()
time.sleep(5)

button = session.find_element(by=By.LINK_TEXT,value="SEARCH JOBS")
button.click()
time.sleep(2)
