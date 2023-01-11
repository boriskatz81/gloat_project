from selenium.webdriver.support import expected_conditions as ec
from Test.Locators.conversion_page_locators import ConversionPageLocators
from Test.Pages.base_class import BaseClass


# This class represents the page we're redirected to once clicking on a specific conversion type
# f.e: Celsius to Faranheit / Ounces to Grams e.t.c
class ConversionPage(BaseClass):

    def __init__(self, driver):
        super(ConversionPage, self).__init__(driver)

    # This function inserts the value we want to convert within the internal textbox
    def insert_value_you_wish_to_convert(self, value_to_convert):
        self.wait.until(ec.element_to_be_clickable(ConversionPageLocators.ARGUMENT_CONV)).send_keys(value_to_convert)

    # This function retrieves the result of the converted value.
    # Since the converted value appears after "=" sign, we return this one, since this what we want to show
    def retrieve_converted_answer(self):
        converted_text = self.wait.until(ec.element_to_be_clickable(ConversionPageLocators.CONVERTED_ANSWER)).text
        return converted_text.split("=")[1]
