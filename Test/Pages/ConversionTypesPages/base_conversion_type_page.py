from selenium.common.exceptions import ElementClickInterceptedException
from Test.Locators.metric_conversion_home_page_locators import MetricConversionHomePageLocators
from Test.Pages.base_class import BaseClass
from selenium.webdriver.support import expected_conditions as ec
from Test.Pages.conversion_page import ConversionPage


# This class is a basic page class - Temperature, Length and Weight page inherit from

class BaseConversionTypePage(BaseClass):

    def __init__(self, driver):
        super(BaseConversionTypePage, self).__init__(driver)

    # This function clicks on relevant conversion type in order to be transfer to the main
    # conversion page. F.E: if we're in Temperature page and click on Celsius to Faranheit
    # Weight page and click on Ounces to Grams e.t.c
    # Parameters:
    # conversion_type_element - attribute of the element we want to click on
    # Since there is an advertisement pop-up constantly appearing at the bottom of the screen
    # and sometimes hides the element we want to click on, we've decided to click on the element several times
    # and if an ElementClickInterceptedException - we try to close the pop-up and try again
    def click_on_conversion_type_you_wish_to_perform(self, conversion_type_element):
        self.click_on_relevant_element_and_if_it_fails_try_close_footer_popup(conversion_type_element)
        return ConversionPage(self.driver)
