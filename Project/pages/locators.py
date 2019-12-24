from selenium.webdriver.common.by import By


class HeaderLocators():
    ABOUT_COMPANY = (By.CSS_SELECTOR, "[title='О компании']")
    CONTACTS = (By.CSS_SELECTOR, "[title='Контакты']")
    SCHEME = (By.CSS_SELECTOR, "[title='Схема проезда']")
    NEWS = (By.CSS_SELECTOR, "[title='Новости компании']")
    LICENSES = (By.CSS_SELECTOR, "[title='Лицензии']")
    PRODUCTS = (By.CSS_SELECTOR, "[title='Продукты']")
    CSP = (By.CSS_SELECTOR, "[href='/products/cryptopro-csp']")
    USING = (By.CSS_SELECTOR, "[href='/products/csp/usage']")
    DEVELOPERS = (By.CSS_SELECTOR, "#quicktabs-tab-1-2")
    DEVELOPERS_GUIDES = (By.CSS_SELECTOR, "#quicktabs_tabpage_1_2 tr td ul li:nth-child(4) a")
class FirstMenuLocators():
    TAG_ABOUT = (By.CSS_SELECTOR, "div h2")
    TAG_CONTACTS = (By.CSS_SELECTOR, "div h2")
    TAG_SCHEME = (By.CSS_SELECTOR, "div h2")
    TAG_NEWS = (By.CSS_SELECTOR, "div h2")
    TAG_LICENSES = (By.CSS_SELECTOR, "div h2")

class SecondMenuLocators():
    TAG_PRODUCTS = (By.CSS_SELECTOR, "div h2")
    TAG_CSP = (By.CSS_SELECTOR, "div h2")

class ThirdMenuLocators():
    TAG_USING = (By.CSS_SELECTOR, "div h2")