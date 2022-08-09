import time

from BaseClass import Base


class HomePage(Base):
    careers = "CAREERS"
    search_jobs = "career-banner-button"

    def __init__(self, session):
        self.session = session

    def navigate_to_careers(self):
        try:
            self.find_element_by_link_text(HomePage.careers).click()
            time.sleep(3)
        except Exception as ex:
            print(f"Failed to navigate to Careers\n{ex}")
            return False

    def navigate_to_job_search(self):
        try:
            self.find_element_by_class(HomePage.search_jobs).click()
            time.sleep(2)
            self.scroll_to_1000()
            time.sleep(3)
        except Exception as ex:
            print(f"Failed to navigate to Careers\n{ex}")
            return False
