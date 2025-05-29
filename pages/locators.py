from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_LINK = (By.LINK_TEXT, "View basket")
    ITEMS_TO_BUY = (By.CLASS_NAME, 'col-sm-6.h3')
    EMPTY_MESSAGE = (By.ID, 'content_inner')


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTRATION_EMAIL = (By.NAME, 'registration-email')
    REGISTRATION_PASSWORD = (By.NAME, 'registration-password1')
    REGISTRATION_PASSWORD_CONFIRM = (By.NAME, 'registration-password2')
    REGISTRATION_BUTTON = (By.NAME, 'registration_submit')


class MainPageLocators():
    # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    pass


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    MESSAGE = (By.CSS_SELECTOR, 'div.alertinner strong')
    PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    TOTAL_PRICE = (By.CSS_SELECTOR, 'div.alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
