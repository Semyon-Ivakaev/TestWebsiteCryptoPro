from selenium.webdriver.common.by import By


class HeaderLocators():
    ABOUT_COMPANY = (By.CSS_SELECTOR, "[title='О компании']")
    CONTACTS = (By.CSS_SELECTOR, "[title='Контакты']")
    SCHEME = (By.CSS_SELECTOR, "[title='Схема проезда']")
    NEWS = (By.CSS_SELECTOR, "[title='Новости компании']")
    LICENSES = (By.CSS_SELECTOR, "[title='Лицензии']")
    PRODUCTS = (By.CSS_SELECTOR, "[title='Продукты']")
    CSP = (By.CSS_SELECTOR, "li .active")

class FirstMenuLocators():
    TAG_ABOUT = (By.CSS_SELECTOR, "div h2")
    TAG_CONTACTS = (By.CSS_SELECTOR, "div h2")
    TAG_SCHEME = (By.CSS_SELECTOR, "div h2")
    TAG_NEWS = (By.CSS_SELECTOR, "div h2")
    TAG_LICENSES = (By.CSS_SELECTOR, "div h2")

class SecondMenuLocators():
    TAG_PRODUCTS = (By.CSS_SELECTOR, "div h2")
    TAG_CSP = (By.CSS_SELECTOR, "div h2")