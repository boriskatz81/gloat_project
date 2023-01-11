import unittest
from Test.Pages.current_weather_home_page import CurrentWeatherHomePage
from Test.Tests.base_test_class import BaseTestClass
from Test.API_Modules.api_modules_class import APIModulesClass


# This class contains the test that enters weather main page, selects required city
# and compares the data received within UI and within appropriate API call for the same city
class WeatherAPIValidationTest(BaseTestClass):
    # The daat of the city, which weather we wish to compare
    city_data = {
        "zip_code": "20852",
        "name": "Bethesda, US",
        "latitude": "39.0461",
        "longitude": "-77.113"
    }

    # This test retrieves the weather data of the required city from API and then converts it
    # to the data, retrieved from UI
    def test_validate_ui_and_api_weather_data(self):
        # Retrieves the API data of the required city weather data
        api_module_class = APIModulesClass()
        api_weather_data = api_module_class.retrieve_api_weather_data(self.city_data)

        # redirects to Weather main page
        driver = self.create_new_driver("https://openweathermap.org/")
        current_weather_home_page = CurrentWeatherHomePage(driver)

        # Within "Search" textbox writes the required city zip-code and selects
        # the required city from drop-down according to its name
        current_weather_home_page.select_city_to_validate_weather(self.city_data)
        ui_weather_data = current_weather_home_page.retrieve_all_weather_data(["Humidity", "Dew point", "Visibility"])
        ui_weather_data["visibility"] = float(ui_weather_data["visibility"]) * 1000
        err_list = []

        # For every data, retrieved from UI weather cell - compare it with its appropriate
        # data from API and if the difference between them is too high - report it
        for key, value in ui_weather_data.items():
            difference = abs(float(ui_weather_data[key]) - float(api_weather_data[key]))
            print(f"{key} - {value} / {api_weather_data[key]} / {float(difference)}")
            if float(difference) > 1:
                err_list.append(f"The difference between UI and API {key} is {int(difference)}")

        # If any high difference reports were detected - fail the test
        assert len(err_list) == 0, f"Mismatch between UI and API weather data - {err_list}"


if __name__ == '__main__':
    unittest.main()
