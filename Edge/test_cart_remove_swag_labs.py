from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from login_data import LoginData
from login_data import ElemLocators
import pytest_check as check
from login_data import items_list
from login_data import cart_button_list
import pytest


class TestUrl:
    url = "https://www.saucedemo.com/v1/index.html"


    @pytest.fixture
    def launch_driver(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Edge(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        yield
        self.driver.close()

    def test_remove_from_cart_standard_user(self, launch_driver):
        self.driver.get(self.url)
        assert self.driver.current_url == "https://www.saucedemo.com/v1/index.html"
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).send_keys(LoginData.user1)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).get_attribute('value') == LoginData.user1
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).send_keys(LoginData.password)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).get_attribute('value') == LoginData.password
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_login).click()
        product = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_product).text
        assert product == 'Products'

        for x in range(6):

            self.driver.find_element(by=By.XPATH, value=(items_list[x-1])).click()

        item_count = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_cart_badge).text
        assert item_count == str(len(items_list))

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_cart).click()

        for index, item_xpath in enumerate(cart_button_list):
            try:
                self.driver.find_element(by=By.XPATH, value=item_xpath).click()
            except NoSuchElementException:
                print("Less Items in Cart then Expected")

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_continueshopping).click()

        try:
            absent_element = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_cart_badge)
        except NoSuchElementException:

            check.is_true(True)
        else:

            check.is_true(False)

        assert product == 'Products'
        assert self.driver.current_url == "https://www.saucedemo.com/v1/inventory.html"


    def test_remove_from_cart_problem_user(self, launch_driver):
        self.driver.get(self.url)
        assert self.driver.current_url == "https://www.saucedemo.com/v1/index.html"
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).send_keys(LoginData.user3)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).get_attribute('value') == LoginData.user3
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).send_keys(LoginData.password)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).get_attribute('value') == LoginData.password
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_login).click()
        product = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_product).text
        assert product == 'Products'

        for index, item_xpath in enumerate(items_list):
            self.driver.find_element(by=By.XPATH, value=item_xpath).click()

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_cart).click()

        for index, item_xpath in enumerate(cart_button_list):
            try:
                self.driver.find_element(by=By.XPATH, value=item_xpath).click()
            except NoSuchElementException:
                print("Less Items in Cart then Expected")

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_continueshopping).click()

        try:
            absent_element = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_cart_badge)
        except NoSuchElementException:

            check.is_true(True)
        else:

            check.is_true(False)

        assert product == 'Products'
        assert self.driver.current_url == "https://www.saucedemo.com/v1/inventory.html"


    def test_remove_from_cart_glitch_user(self, launch_driver):
        self.driver.get(self.url)
        assert self.driver.current_url == "https://www.saucedemo.com/v1/index.html"
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).send_keys(LoginData.user4)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).get_attribute('value') == LoginData.user4
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).send_keys(LoginData.password)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).get_attribute('value') == LoginData.password
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_login).click()
        product = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_product).text
        assert product == 'Products'

        for x in range(6):

            self.driver.find_element(by=By.XPATH, value=(items_list[x-1])).click()

        item_count = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_cart_badge).text
        assert item_count == str(len(items_list))

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_cart).click()

        for index, item_xpath in enumerate(cart_button_list):
            try:
                self.driver.find_element(by=By.XPATH, value=item_xpath).click()
            except NoSuchElementException:
                print("Less Items in Cart then Expected")

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_continueshopping).click()

        try:
            absent_element = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_cart_badge)
        except NoSuchElementException:

            check.is_true(True)
        else:

            check.is_true(False)

        assert product == 'Products'
        assert self.driver.current_url == "https://www.saucedemo.com/v1/inventory.html"