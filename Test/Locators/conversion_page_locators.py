from selenium.webdriver.common.by import By


# This class represents all required elements within General Conversion Page,
# we're redirected to after clicking f.e: celsius -> faranheit, meters -> feet e.t.c
class ConversionPageLocators(object):
    ARGUMENT_CONV = By.CSS_SELECTOR, 'input[id="argumentConv"]'
    CONVERTED_ANSWER = By.CSS_SELECTOR, '[id="answer"]'
