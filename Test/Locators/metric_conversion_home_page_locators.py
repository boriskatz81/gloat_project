from selenium.webdriver.common.by import By

# This class represents all the required elements within Metric Conversion page
# we've first redirected to when starting conversions tests
class MetricConversionHomePageLocators(object):
    TEMPERATURE = By.CSS_SELECTOR, 'a[href="/temperature-conversion.htm"]'
    WEIGHT = By.CSS_SELECTOR, 'a[href="/weight-conversion.htm"]'
    LENGTH = By.CSS_SELECTOR, 'a[href="/length-conversion.htm"]'
    FOOTER_POPUP_CLOSE_BUTTON = By.CSS_SELECTOR, 'span[id="ezmob-footer-close"]'
