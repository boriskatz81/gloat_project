from selenium.webdriver.common.by import By


# This class represents all the required elements within "Weather" page, we;re redirected to
# when starting Weather comparison tests
class CurrentWeatherHomePageLocators(object):
    SEARCH_TEXTBOX = By.CSS_SELECTOR, 'input[placeholder="Search city"]'
    SEARCH_BUTTON = By.CSS_SELECTOR, 'button[type="submit"]'

    CURRENT_TEMP = By.CSS_SELECTOR, '[class="current-temp"]'
    WIND_LINE = By.CSS_SELECTOR, '[class="wind-line"]'
    PRESSURE = By.XPATH, '//*[@class="icon-pressure"]/..'

    # This function returns the XPATH of the element within UI weather data,
    # according to its text - f.e: Humidity, Wind Speed etc
    @staticmethod
    def relevant_weather_data_from_a_specific_icon(icon_title):
        return By.XPATH, f'//span[@class="symbol" and text() = "{icon_title}"]/..'

    # This function returns the XPATH of the required "city name" element within drop-down options
    # after writing its zip-code within Weather Page Search textbox
    @staticmethod
    def relevant_city_name_within_drop_down(city_name):
        return By.XPATH, f'//*[@class="search-dropdown-menu"]//span[normalize-space(text()) ="{city_name}"]'

    # This function returns the cell within Weather Page according to the required city name
    # This is done when selecting the required city within search drop-down
    # and ensuring the city name and its data has changed below before continuing the test
    @staticmethod
    def relevant_city_name_within_weather_cell(city_name):
        return By.XPATH, f'//div[@class="current-container mobile-padding"]//*[text() ="{city_name}"]'
