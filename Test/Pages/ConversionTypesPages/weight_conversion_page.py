from Test.Pages.ConversionTypesPages.base_conversion_type_page import BaseConversionTypePage


# This class is a page we're redirected to when clicking "Weight" within Metric conversion main page
# It us empty, since there is nothing we need to do within this page for this test, apart from clicking
# on appropriate conversion type element, function which already appears within BaseConversionTypePage,
# this class inherits from. However, we still decided to create this class, in case we'll perform something
# within this class in the future
class WeightConversionPage(BaseConversionTypePage):

    def __init__(self, driver):
        super(WeightConversionPage, self).__init__(driver)
