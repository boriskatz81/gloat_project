from selenium.webdriver.common.by import By


# This class contains all required elements within "Temperature" page
class TemperatureConversionPageLocators(object):
    CELSIUS_TO_FAHRENHEIT = By.CSS_SELECTOR, 'a[href="/temperature/celsius-to-fahrenheit.htm"]'


# This class contains all required elements within "Length" page
class LengthConversionPageLocators(object):
    METERS_TO_FEET = By.CSS_SELECTOR, 'a[href="/length/meters-to-feet.htm"]'


# This class contains all required elements within "Weight" page
class WeightConversionPageLocators(object):
    OUNCES_TO_GRAMS = By.CSS_SELECTOR, 'a[href="/weight/ounces-to-grams.htm"]'
