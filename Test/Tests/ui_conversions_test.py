import unittest
from Test.Locators.all_conversion_types_pages_locators import TemperatureConversionPageLocators, \
    LengthConversionPageLocators, WeightConversionPageLocators
from Test.Pages.metric_conversion_home_page import MetricConversionHomePage
from Test.Tests.base_test_class import BaseTestClass


# This class contains 3 tests. All 3 of them enter "Metrics Conversion" main page, entering appropriate
# conversion type page (temperature / weight/ length e.t.c), enters conversion type within the selected type
# (f.e: if temperature -> celsius to fahrenheit, if length -> meters to feet e.t.c) and, once inside
# the general conversion page, inserts the value we wish to convert, retrieve the converted answer
# and print it
class UIConversionsTest(BaseTestClass):

    # This function creates a new Chrome Driver, redirects it to Metric Conversion page
    # and returns Metric Conversion page instance
    def create_new_driver_and_metric_conversion_home_page(self):
        driver = self.create_new_driver("https://www.metric-conversions.org/")
        metric_conversion_home_page = MetricConversionHomePage(driver)
        return driver, metric_conversion_home_page

    # This function completes the entire conversion process.
    # 1. Enters the appropriate conversion type from the selected type before
    # 2. Within the textbox in the general Conversion page - insert the value we wish to convert
    # 3. Retrieve the converted value from the object below
    # 4. Printing the initial and the converted values
    # Parameters:
    # conversion_type_element - conversion type to click on in order to be redirected to the general conversion page
    # (f.e: if temperature -> celsius to fahrenheit, if length -> meters to feet e.t.c)
    # conversion_type_page - Conversion type page we've been redirected from Metric Conversion page
    # (f.e: temperature / length e.t.c)
    # value_to_convert - value we want to convert
    # conversion_type_symbol - the symbol of value_to_convert in order to print at the end of the function
    # (f.e: meters, ounces e.t.c)
    def complete_conversion_process(self, conversion_type_element, conversion_type_page, value_to_convert,
                                    conversion_type_symbol):
        conversion_page = conversion_type_page.click_on_conversion_type_you_wish_to_perform(conversion_type_element)
        conversion_page.insert_value_you_wish_to_convert(value_to_convert)
        converted_value = conversion_page.retrieve_converted_answer()
        print(f"{value_to_convert}{conversion_type_symbol} is {converted_value}")

    # This tests converts Celsius to Fahrenheit from Metric Conversion main page
    def test_convert_celsius_to_fahrenheit(self):
        driver, metric_conversion_home_page = self.create_new_driver_and_metric_conversion_home_page()
        self.complete_conversion_process(TemperatureConversionPageLocators.CELSIUS_TO_FAHRENHEIT,
                                         metric_conversion_home_page.click_on_temperature(),
                                         "30", "°")
        driver.close()

    # This tests converts Meters to Feet from Metric Conversion main page
    def test_convert_meters_to_feet(self):
        driver, metric_conversion_home_page = self.create_new_driver_and_metric_conversion_home_page()
        self.complete_conversion_process(LengthConversionPageLocators.METERS_TO_FEET,
                                         metric_conversion_home_page.click_on_length(),
                                         "20", "meters")

        driver.close()

    # This tests converts Ounces to Grams from Metric Conversion main page
    def test_convert_ounces_to_grams(self):
        driver, metric_conversion_home_page = self.create_new_driver_and_metric_conversion_home_page()
        self.complete_conversion_process(WeightConversionPageLocators.OUNCES_TO_GRAMS,
                                         metric_conversion_home_page.click_on_weight(),
                                         "850", "ounces")

        driver.close()


if __name__ == '__main__':
    unittest.main()
