import time
import pytest
from .pages.main_page import MainPage
from .pages.base_page import BasePage


class TestCrypto:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://www.ctm.ru/"

    @pytest.mark.skip
    def test_guest_go_to_about_company(self, browser):
        link = "https://www.cryptopro.ru/"
        page = MainPage(browser, link)
        page.open()
        page.guest_go_to_about_company()
        print("Test is Ok")

    @pytest.mark.skip
    def test_guest_go_to_contacts(self, browser):
        link = "https://www.cryptopro.ru/"
        page = MainPage(browser, link)
        page.open()
        page.guest_go_to_contacts()

    @pytest.mark.skip
    def test_guest_go_to_scheme(self, browser):
        link = "https://www.cryptopro.ru/"
        page = MainPage(browser, link)
        page.open()
        page.guest_go_to_scheme()

    @pytest.mark.skip
    def test_guest_go_to_news(self, browser):
        link = "https://www.cryptopro.ru/"
        page = MainPage(browser, link)
        page.open()
        page.guest_go_to_news()

    @pytest.mark.skip
    def test_guest_go_to_licenses(self, browser):
        link = "https://www.cryptopro.ru/"
        page = MainPage(browser, link)
        page.open()
        page.guest_go_to_licenses()

    @pytest.mark.skip
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