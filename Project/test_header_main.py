import time
import pytest
from .pages.main_page import MainPage
from .pages.base_page import BasePage


class TestCrypto:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://www.ctm.ru/"


    def test_guest_go_to_about_company(self, browser):
        link = "https://www.cryptopro.ru/"
        page = MainPage(browser, link)
        page.open()
        page.guest_go_to_about_company()
        print("Test is Ok")


    def test_guest_go_to_contacts(self, browser):
        link = "https://www.cryptopro.ru/"
        page = MainPage(browser, link)
        page.open()
        page.guest_go_to_contacts()


    def test_guest_go_to_scheme(self, browser):
        link = "https://www.cryptopro.ru/"
        page = MainPage(browser, link)
        page.open()
        page.guest_go_to_scheme()


    def test_guest_go_to_news(self, browser):
        link = "https://www.cryptopro.ru/"
        page = MainPage(browser, link)
        page.open()
        page.guest_go_to_news()


    def test_guest_go_to_licenses(self, browser):
        link = "https://www.cryptopro.ru/"
        page = MainPage(browser, link)
        page.open()
        page.guest_go_to_licenses()


    def test_guest_go_to_product(self, browser):
        link = "https://www.cryptopro.ru/"
        page = MainPage(browser, link)
        page.open()
        page.guest_go_to_products()


    def test_guest_go_to_CSP(self, browser):
        link = "https://www.cryptopro.ru/"
        page = MainPage(browser, link)
        page.open()
        page.guest_go_to_CSP()


    def test_guest_go_to_using(self, browser):
        link = "https://www.cryptopro.ru/"
        page = MainPage(browser, link)
        page.open()
        page.guest_go_to_using()

    def test_guest_click_on_developers(self, browser):
        link = "https://www.cryptopro.ru/"
        page = MainPage(browser, link)
        page.open()
        page.guest_click_on_developers()