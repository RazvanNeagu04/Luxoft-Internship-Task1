from lib_luxoft_com.Home_Page import home_page
from lib_luxoft_com.Base_Page import base
from lib_luxoft_com.caeersPage import job_search

basic = base()
session = basic.session
home = home_page(session)
job = job_search(session)

basic.navigate_to("https://www.luxoft.com")

basic.maximize()

home.navigate_to_careers()

accept_button = session.find_element_by_xpath(job.accept_button).click()


home.navigate_to_job_search()

job.set_job_filters(country="Romania", city="Bucharest", specialization="QA Automation")

job.count_offers()
