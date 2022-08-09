from Home_Page import HomePage
from BaseClass import Base
from careersPage import jobSearch

basic = Base()
browser_session = basic.session
home = HomePage(browser_session)
job = jobSearch(browser_session)

basic.navigate_to("https://www.luxoft.com")

basic.maximize()

home.navigate_to_careers()

home.navigate_to_job_search()

job.set_job_filters(country="Romania", city="Bucharest", specialization="QA Automation")

job.count_offers()
