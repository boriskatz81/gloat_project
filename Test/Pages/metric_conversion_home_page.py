from Test.Locators.metric_conversion_home_page_locators import MetricConversionHomePageLocators
from Test.Pages.ConversionTypesPages.length_conversion_page import LengthConversionPage
from Test.Pages.ConversionTypesPages.temperature_conversion_page import TemperatureConversionPage
from Test.Pages.ConversionTypesPages.weight_conversion_page import WeightConversionPage
from Test.Pages.base_class import BaseClass


# This is the first page we're redirected when opening a browser for "Conversions" tests
class MetricConversionHomePage(BaseClass):

    def __init__(self, driver):
        super(MetricConversionHomePage, self).__init__(driver)

    # Clicks on "Temperature" icon within the table options
    def click_on_temperature(self):
        self.click_on_relevant_element_and_if_it_fails_try_close_footer_popup(MetricConversionHomePageLocators.TEMPERATURE)
        return TemperatureConversionPage(self.driver)

    # Clicks on "Weight" icon within the table options
    def click_on_weight(self):
        self.click_on_relevant_element_and_if_it_fails_try_close_footer_popup(MetricConversionHomePageLocators.WEIGHT)
        return WeightConversionPage(self.driver)

    # Clicks on "Length" icon within the table options
    def click_on_length(self):
        self.click_on_relevant_element_and_if_it_fails_try_close_footer_popup(MetricConversionHomePageLocators.LENGTH)
        return LengthConversionPage(self.driver)
