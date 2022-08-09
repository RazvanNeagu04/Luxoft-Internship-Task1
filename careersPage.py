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
from baseclass import Base

class job_search(Base):
    country_filter="//span[contains(text(),'Countries')]/.."
    country_input="//span[contains(@aria-owns, 'search_countries')]//input"
    city_filter="//span[contains(text(),'Cities')]/.."
    city_input="//span[contains(@aria-owns, 'search_cities')]//input"
    specialization_filter="//span[contains(text(),'Specializations')]/.."
    specialization_input="//span[contains(@aria-owns, 'search_type')]//input"
    search_button="save-country-ids"
    offers="//tr[contains(@data-offers-id,'')]"
    next_page="previous_page"
    accept_button="//tr[contains(@data-offers-id,'')]"