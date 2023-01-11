from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Test.Locators.metric_conversion_home_page_locators import MetricConversionHomePageLocators


# This is the base page class, every page heritages from.
# It sets the relevant page Chrome driver and "wait" timeout
class BaseClass:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.long_wait = WebDriverWait(self.driver, 60)

    # This function clicks on relevant element in order to be redirected to the next page
    # Parameters:
    # element_attribute - attribute of the element we want to click on
    # Since there is an advertisement pop-up constantly appearing at the bottom of the screen
    # and sometimes hides the element we want to click on, we've decided to click on the element several times
    # and if an ElementClickInterceptedException - we try to close the pop-up and try again
    def click_on_relevant_element_and_if_it_fails_try_close_footer_popup(self, element_attribute):
        times_to_try = 30
        for i in range(times_to_try):
            try:
                self.wait.until(ec.element_to_be_clickable(element_attribute)).click()
                return

            except ElementClickInterceptedException:
                try:
                    self.wait.until(
                        ec.element_to_be_clickable(MetricConversionHomePageLocators.FOOTER_POPUP_CLOSE_BUTTON)).click()
                except:
                    print("No advert pop-up appeared")

        self.wait.until(ec.element_to_be_clickable(element_attribute)).click()
