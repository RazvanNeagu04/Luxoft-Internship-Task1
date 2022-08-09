import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class Base():
    def __init__(self):
        chrome_options = Options()
        chrome_options.binary_location = "C://Program Files//Google//Chrome Beta//Application//chrome.exe"
        self.session = webdriver.Chrome(service=Service(ChromeDriverManager('104.0.5112.20').install()),
                                   options=chrome_options)

    def maximize(self):
        self.session.maximize_window()

    def scroll_to_value(self):
        try:
            self.session.execute_script("window.scrollTo(0, 1200)")
        except Exception as  e:
            print("scroll to value has failed. Error:"+ str(e))
            return False
        return True

    def find_element_by_link_text(self, element):
        try:
            value = self.session.find_element(by=By.LINK_TEXT, value=element)

        except:
            return False
        return value

    def find_element_by_xpath(self, element):
       try:
            value = self.session.find_element(by=By.XPATH, value=element)

       except:
            return False

       return value

    def find_elements_by_xpath(self, element):
       try:
            value = self.session.find_elements(by=By.XPATH, value=element)

       except:
            return False

       return value

    def find_element_by_class(self, element):
        try:
            value = self.session.find_element(by=By.CLASS_NAME, value=element)

        except:
            return False

        return value



    def find_element_by_id(self, element):
        try:
            value = self.session.find_element(by=By.ID, value=element)

        except:
            return False

        return value

    def navigate_to(self, url):
        try:
            self.session.get(url)
        except:
            print("Navigate has failed")
            return False
        return True




