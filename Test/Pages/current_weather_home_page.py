import time
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as ec
from Test.Locators.current_weather_home_page_locators import CurrentWeatherHomePageLocators
import re
from Test.Pages.base_class import BaseClass


# This is the main weather page, we're initially redirected to, when performing Weather comparison tests
class CurrentWeatherHomePage(BaseClass):

    def __init__(self, driver):
        super(CurrentWeatherHomePage, self).__init__(driver)

    # This function clicks on "Submit" button, once writing the required city zip-code
    # Since, page loading sometimes takes too long, causing the Submit button to be unclickable
    # we perform it several times, before failing the test
    def click_on_submit(self):
        times_to_try = 30
        for i in range(times_to_try):
            try:
                self.wait.until(ec.element_to_be_clickable(CurrentWeatherHomePageLocators.SEARCH_BUTTON)).click()
                return
            except ElementClickInterceptedException:
                time.sleep(2)

        self.wait.until(ec.element_to_be_clickable(CurrentWeatherHomePageLocators.SEARCH_BUTTON)).click()

    # This function writes the zip-code of the required city and clicking on Submit for the drop-down
    # to be opened
    def write_zip_code_and_click_submit(self, zip_code):
        self.wait.until(ec.element_to_be_clickable(CurrentWeatherHomePageLocators.SEARCH_TEXTBOX)).send_keys(zip_code)
        self.click_on_submit()

    # This function selects the appropriate city, according to its name, once its zip-code
    # was written amd Submit button was clicked
    def select_appropriate_city_from_drop_down(self, city_name):
        # selecting the appropriate city, according to its name
        self.wait.until(
            ec.element_to_be_clickable(
                CurrentWeatherHomePageLocators.relevant_city_name_within_drop_down(city_name))).click()

        # Waiting until the cell below (where temperature is presented) has updated
        # to the required city
        self.wait.until(
            ec.element_to_be_clickable(
                CurrentWeatherHomePageLocators.relevant_city_name_within_weather_cell(city_name)))

    # Writing zip-code within Search textbox, clicking on Submit and select required
    # city from drop-down
    def select_city_to_validate_weather(self, city_data):
        self.write_zip_code_and_click_submit(city_data["zip_code"])
        self.select_appropriate_city_from_drop_down(city_data["name"])

    # This function retrieves all the weather data within the cell of the required city, which
    # we later compare with the API one
    # Parameters:
    # additional_data_to_compare - additional data from the table (apart from "Current Temperature" ,
    # "Wind Line" and "Pressure") we want to retrieve and compare with API data
    def retrieve_all_weather_data(self, additional_data_to_compare):
        weather_data = {}
        # first retrieving and storing the data from the elements that have unique attribute (id / class e.t.c)
        # Those are "Current Temperature" , "Wind Line" and "Pressure"
        current_temp = self.wait.until(ec.element_to_be_clickable(CurrentWeatherHomePageLocators.CURRENT_TEMP)).text
        wind_line = self.wait.until(ec.element_to_be_clickable(CurrentWeatherHomePageLocators.WIND_LINE)).text
        pressure = self.wait.until(ec.element_to_be_clickable(CurrentWeatherHomePageLocators.PRESSURE)).text
        weather_data.update({"temp": current_temp, "pressure": pressure, "wind_speed": wind_line})

        # Retrieving the values from all the elements that are detected according to the texts within
        # additional_data_to_compare dict and add it to the data to return for further comparison
        for data_to_compare in additional_data_to_compare:
            additional_icon_value = \
                self.wait.until(
                    ec.element_to_be_clickable(
                        CurrentWeatherHomePageLocators.relevant_weather_data_from_a_specific_icon(
                            f'{data_to_compare}:'))).text

            additional_icon_value = additional_icon_value.split("\n")[1]
            weather_data.update({data_to_compare.lower().replace(" ", "_"): additional_icon_value})

        # Remove all necessary characters from the retrieved and stored values, so only numeric values will remain
        # r'[A-Za-z°%/]' was selected in order not to remove "-" (negative value) and "." (decimal sign) characters
        for key, value in weather_data.items():
            weather_data[key] = re.sub(r'[A-Za-z°%/]', "", weather_data[key]).strip()

        return weather_data
