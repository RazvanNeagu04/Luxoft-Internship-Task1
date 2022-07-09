# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver-manager import ChromeDriverManager
#
# session = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
# session.get(url = "https://www.luxoft.com")
#
# time.sleep(5)
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

session = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
session.get(url="https://www.luxoft.com")

time.sleep(5)