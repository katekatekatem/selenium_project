from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_products_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.ITEMS_TO_BUY
        ), "Products are in basket, but should not be"

    def should_be_message_about_empty_basket(self):
        assert "Your basket is empty" in self.browser.find_element(
            *BasketPageLocators.EMPTY_MESSAGE
        ).text, "Empty message is not present, but should be"
