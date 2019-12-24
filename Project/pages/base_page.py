from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from .locators import HeaderLocators, FirstMenuLocators, SecondMenuLocators, ThirdMenuLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pytest


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def guest_go_to_about_company(self):
        self.browser.find_element(*HeaderLocators.ABOUT_COMPANY).click()
        time.sleep(3)
        check = self.browser.find_element(*FirstMenuLocators.TAG_ABOUT).text
        assert check == "О компании", 'Message - "О компании" on page not found'

    def guest_go_to_contacts(self):
        action = ActionChains(self.browser)  # ActionChains нужен для мышки
        Open_first_menu = self.browser.find_element(*HeaderLocators.ABOUT_COMPANY)
        action.move_to_element(Open_first_menu).perform()  # это делает наводку на меню и открывает список
        self.browser.find_element(*HeaderLocators.CONTACTS).click()
        check = self.browser.find_element(*FirstMenuLocators.TAG_CONTACTS).text
        assert check == "Контакты", 'Message - "Контакты" on page not found'

    def guest_go_to_scheme(self):
        action = ActionChains(self.browser)
        Open_first_menu = self.browser.find_element(*HeaderLocators.ABOUT_COMPANY)
        action.move_to_element(Open_first_menu).perform()
        self.browser.find_element(*HeaderLocators.SCHEME).click()
        check = self.browser.find_element(*FirstMenuLocators.TAG_SCHEME).text
        assert check == "Схема проезда", 'Message - "Схема проезда" on page not found'

    def guest_go_to_news(self):
        action = ActionChains(self.browser)
        Open_first_menu = self.browser.find_element(*HeaderLocators.ABOUT_COMPANY)
        action.move_to_element(Open_first_menu).perform()
        self.browser.find_element(*HeaderLocators.NEWS).click()
        check = self.browser.find_element(*FirstMenuLocators.TAG_NEWS).text
        assert check == "Новости КриптоПро", 'Message - "Новости КриптоПро" on page not found'

    def guest_go_to_licenses(self):
        action = ActionChains(self.browser)
        Open_first_menu = self.browser.find_element(*HeaderLocators.ABOUT_COMPANY)
        action.move_to_element(Open_first_menu).perform()
        self.browser.find_element(*HeaderLocators.LICENSES).click()
        check = self.browser.find_element(*FirstMenuLocators.TAG_LICENSES).text
        assert check == "Лицензии", 'Message - "Лицензии" on page not found'

    def guest_go_to_products(self):
        self.browser.find_element(*HeaderLocators.PRODUCTS).click()
        check = self.browser.find_element(*SecondMenuLocators.TAG_PRODUCTS).text
        assert check == "Продукты", 'Message - "Продукты" on page not found'

    def guest_go_to_CSP(self):
        action = ActionChains(self.browser)
        Open_second_menu = self.browser.find_element(*HeaderLocators.PRODUCTS)
        action.move_to_element(Open_second_menu).perform()
        self.browser.find_element(*HeaderLocators.CSP).click()
        check = self.browser.find_element(*SecondMenuLocators.TAG_CSP).text
        assert check == "КриптоПро CSP", 'Message - "КриптоПро CSP" on page not found'

    def guest_go_to_using(self):
        action = ActionChains(self.browser)
        Open_second_menu = self.browser.find_element(*HeaderLocators.PRODUCTS)
        action.move_to_element(Open_second_menu).perform()
        Open_third_menu = self.browser.find_element(*HeaderLocators.CSP)
        action.move_to_element(Open_third_menu).perform()
        self.browser.find_element(*HeaderLocators.USING).click()
        check = self.browser.find_element(*ThirdMenuLocators.TAG_USING).text
        assert check == "Использование КриптоПро CSP",  'Message - "Использование КриптоПро CSP" on page not found'

    def guest_click_on_developers(self):
        self.browser.find_element(*HeaderLocators.DEVELOPERS).click()
        check = self.browser.find_element(*HeaderLocators.DEVELOPERS_GUIDES).text
        print(check)
        assert check == "Руководства разработчика", 'Message - "Руководства разработчика" on page not found'