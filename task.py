
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

session = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
session.get(url="https://www.luxoft.com")

session.maximize_window()
time.sleep(10)

button = session.find_element_by_link_text("Careers")
button.click

session.find_element()

time.sleep(5)

