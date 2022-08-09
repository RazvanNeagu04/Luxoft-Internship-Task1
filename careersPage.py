import time

from selenium.webdriver.common.keys import Keys

from BaseClass import Base


class jobSearch(Base):
    countryFilter = "//select[@id= 'search_countries']/.."
    countryInput = "//span[contains(@aria-owns, 'search_countries')]//input"
    cityFilter = "//select[@id='search_cities']/.."
    cityInput = "//span[contains(@aria-owns, 'search_cities')]//input"
    specializationFilter = "//select[@id='search_type']/.."
    specializationInput = "//span[contains(@aria-owns, 'search_type')]//input"
    searchButton = "save-country-ids"
    offers = "//tr[contains(@data-offers-id,'')]"
    nextPage = "previous_page"

    def __init__(self, session):
        self.session = session

    def set_job_filters(self, country=None, city=None, specialization=None):
        known_countries = ["Argentina", "Australia", "Brazil", "Bulgaria", "Canada", "Chile", "China", "Egypt",
                           "Estonia", "France", "Germany", "Hong Kong", "Hungary", "India", "Ireland", "Italy", "Japan",
                           "Republic of Korea", "Malaysia", "Mexico", "Netherlands", "Poland", "Qatar", "romania",
                           "Saudi Arabia", "Serbia", "Singapore", "South Africa", "Spain", "Sri Lanka", "Sweden",
                           "Switzerland", "Turkey", "Ukraine", "United Arab Emirates", "United Kingdom",
                           "United States", "Vietnam"]
        # Set Filters
        if country:
            if country.lower() not in known_countries:
                print("Error - Unknown Country")
                return False
            try:
                self.find_element_by_xpath(jobSearch.countryFilter).click()
                countries = self.find_element_by_xpath(jobSearch.countryInput)
                countries.send_keys(country)
                countries.send_keys(Keys.ENTER)
                time.sleep(3)
            except Exception as ex:
                print(f"Error - Failed to set country as filter: {ex} ")
                return False
        if city:
            try:
                self.find_element_by_xpath(jobSearch.cityFilter).click()
                cities = self.find_element_by_xpath(jobSearch.cityInput)
                cities.send_keys(city)
                cities.send_keys(Keys.ENTER)
                time.sleep(3)
            except Exception as ex:
                print(f"Error - Failed to set city as filter: {ex} ")
                return False
        if specialization:
            try:
                self.find_element_by_xpath(jobSearch.specializationFilter).click()
                keyword = self.find_element_by_xpath(jobSearch.specializationInput)
                keyword.send_keys(specialization)
                keyword.send_keys(Keys.ENTER)
                time.sleep(3)
            except Exception as ex:
                print(f"Error - Failed to set specialization as filter: {ex} ")
                return False
        # Click Search Jobs by filter
        self.find_element_by_id(jobSearch.searchButton).click()
        time.sleep(3)

    def count_offers(self):
        try:
            offers_page1 = self.find_elements_by_xpath(jobSearch.offers)
            self.scroll_to_1000()
            time.sleep(2)
            self.find_element_by_id(jobSearch.nextPage).click()
            time.sleep(2)
            offers_page2 = self.find_elements_by_xpath(jobSearch.offers)
            print("Numarul total de oferte este: ", len(offers_page1) + len(offers_page2) - 2)
            time.sleep(5)
        except Exception as ex:
            print(f"Error - Failed to count offers, {ex}")
            return False
