import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Base:
    def __init__(self):
        chrome_options = Options()
        chrome_options.binary_location = "C://Program Files//Google//Chrome Beta//Application//chrome.exe"
        self.session = webdriver.Chrome(service=Service(ChromeDriverManager('104.0.5112.20').install()),
                                        options=chrome_options)

    def navigate_to(self, url):
        try:
            self.session.get(url)
            time.sleep(3)
        except Exception as ex:
            print(f"Error - Failed navigation to designated URL: {ex}")
            return False

    def maximize(self):
        try:
            self.session.maximize_window()
            time.sleep(2)
        except Exception as ex:
            print(f"Error - Failed to maximize window: {ex}")
            return False

    def scroll_to_1000(self):
        try:
            self.session.execute_script("window.scrollTo(0, 1000)")
        except Exception as ex:
            print(f"Error - Failed to scroll: {ex}")
            return False

    def find_element_by_link_text(self, element):
        try:
            value = self.session.find_element(by=By.LINK_TEXT, value=element)
            return value
        except Exception as ex:
            print(f"Error - Failed to find element by Link Text: {ex}")
            return False

    def find_element_by_class(self, element):
        try:
            value = self.session.find_element(by=By.CLASS_NAME, value=element)
            return value
        except Exception as ex:
            print(f"Error - Failed to find element by Class: {ex}")
            return False

    def find_element_by_xpath(self, element):
        try:
            value = self.session.find_element(by=By.XPATH, value=element)
            return value
        except Exception as ex:
            print(f"Error - Failed to find element by XPath, {ex}")
            return False

    def find_element_by_id(self, element):
        try:
            value = self.session.find_element(by=By.ID, value=element)
            return value
        except Exception as ex:
            print(f"Error - Failed to find element by ID, {ex}")
            return False

    def find_elements_by_xpath(self, element):
        try:
            value = self.session.find_elements(by=By.XPATH, value=element)
            return value
        except Exception as ex:
            print(f"Error - Failed to find elements by XPath, {ex}")
            return False
