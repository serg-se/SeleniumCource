from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        ), "Add to basket button is not presented"

    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket.click()

    def product_added_to_basket(self):
        alerts = self.browser.find_elements(*ProductPageLocators.BASKET_ALERTS_SUCCESS)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert product_name.text in (alert.text for alert in alerts)

    def basket_price_is_correct(self):
        alerts = self.browser.find_elements(*ProductPageLocators.BASKET_ALERTS_INFO)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert product_price.text in (alert.text for alert in alerts)

    def success_message_is_not_present(self):
        assert self.is_not_element_present(
            *ProductPageLocators.BASKET_ALERTS_SUCCESS
        ), "Success message is present"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.BASKET_ALERTS_SUCCESS
        ), "Success message did not disappear"
