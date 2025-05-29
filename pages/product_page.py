from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def product_name_should_be_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        message = self.browser.find_element(*ProductPageLocators.MESSAGE)
        assert product_name.text == message.text, "Product name is not the same in the basket"

    def product_price_should_be_the_same_in_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE)
        total_price = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE)
        assert product_price.text == total_price.text, "Product price is not the same in the basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is not disappeared, but should"
