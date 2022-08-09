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


class Home_Page():
    careers = "CAREERS"
    search_jobs= "career-banner-button"

    def __init__(self, session:webdriver):
        self.session = session


    def navigate_to_careers(self):
        try:
            button = self.session.find_element_by_link_text(Home_Page.careers).click()
            # click the button
            return True
        except Exception as ex:
            print(f"Failed to navigate to Careers\n{ex}")
            return False
