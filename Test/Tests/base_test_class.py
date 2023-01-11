import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# This is the class all Test classes heritages from.
# It creates a new chrome driver, sets its implicit wait, page loading timeout, maximize it,
# redirects to thr given url and returns it for further test progress
class BaseTestClass(unittest.TestCase):
    def create_new_driver(self, url):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.set_page_load_timeout(100)
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(url)
        return driver