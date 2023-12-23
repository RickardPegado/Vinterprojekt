from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from login_data import LoginData
from login_data import ElemLocators
from login_data import CartData
import pytest_check as check
from login_data import items_list
from login_data import cart_button_list
from login_data import items_desc_list
from time import sleep as wait
import pytest


class TestUrl:
    url = "https://www.saucedemo.com/v1/index.html"


    @pytest.fixture
    def launch_driver(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        yield
        self.driver.close()

    def test_checkout_standard_user(self, launch_driver):
        self.driver.get(self.url)
        assert self.driver.current_url == "https://www.saucedemo.com/v1/index.html"
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).send_keys(LoginData.user1)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).get_attribute('value') == LoginData.user1
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).send_keys(LoginData.password)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).get_attribute('value') == LoginData.password
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_login).click()
        product = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_product).text
        assert product == 'Products'

        
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_backpack).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_bike).click()

        item_count = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_cart_badge).text
        assert item_count == '2'
    
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_cart).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_checkout).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_firstname).send_keys(CartData.firstname)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_firstname).get_attribute('value') == CartData.firstname
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_lastname).send_keys(CartData.lastname)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_lastname).get_attribute('value') == CartData.lastname
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_zipcode).send_keys(CartData.zipcode)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_zipcode).get_attribute('value') == CartData.zipcode
        
        
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_continue).click()
        cart_total = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_total).text
        product_total = CartData.product_rate1 + CartData.product_rate2 + CartData.tax1
        assert cart_total == 'Total: $' + str(round(product_total, 2))

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_finish).click()
        confirm = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_confirm).text
        assert confirm == 'THANK YOU FOR YOUR ORDER'

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_menu).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_logout).click()

        assert self.driver.current_url == 'https://www.saucedemo.com/v1/index.html'


    def test_checkout_problem_user(self, launch_driver):
        self.driver.get(self.url)
        assert self.driver.current_url == "https://www.saucedemo.com/v1/index.html"
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).send_keys(LoginData.user3)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).get_attribute('value') == LoginData.user3
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).send_keys(LoginData.password)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).get_attribute('value') == LoginData.password
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_login).click()
        product = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_product).text
        assert product == 'Products'

        
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_backpack).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_bike).click()

        item_count = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_cart_badge).text
        assert item_count == '2'
    
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_cart).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_checkout).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_firstname).send_keys(CartData.firstname)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_firstname).get_attribute('value') == CartData.firstname
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_lastname).send_keys(CartData.lastname)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_lastname).get_attribute('value') == CartData.lastname
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_zipcode).send_keys(CartData.zipcode)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_zipcode).get_attribute('value') == CartData.zipcode
        
        
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_continue).click()
        cart_total = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_total).text
        product_total = CartData.product_rate1 + CartData.product_rate2 + CartData.tax1
        assert cart_total == 'Total: $' + str(round(product_total, 2))

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_finish).click()
        confirm = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_confirm).text
        assert confirm == 'THANK YOU FOR YOUR ORDER'

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_menu).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_logout).click()

        assert self.driver.current_url == 'https://www.saucedemo.com/v1/index.html'


    def test_checkout_glitch_user(self, launch_driver):
        self.driver.get(self.url)
        assert self.driver.current_url == "https://www.saucedemo.com/v1/index.html"
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).send_keys(LoginData.user4)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).get_attribute('value') == LoginData.user4
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).send_keys(LoginData.password)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).get_attribute('value') == LoginData.password
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_login).click()
        product = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_product).text
        assert product == 'Products'

        
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_backpack).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_bike).click()

        item_count = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_cart_badge).text
        assert item_count == '2'
    
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_cart).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_checkout).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_firstname).send_keys(CartData.firstname)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_firstname).get_attribute('value') == CartData.firstname
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_lastname).send_keys(CartData.lastname)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_lastname).get_attribute('value') == CartData.lastname
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_zipcode).send_keys(CartData.zipcode)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_zipcode).get_attribute('value') == CartData.zipcode
        
        
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_continue).click()
        cart_total = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_total).text
        product_total = CartData.product_rate1 + CartData.product_rate2 + CartData.tax1
        assert cart_total == 'Total: $' + str(round(product_total, 2))

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_finish).click()
        confirm = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_confirm).text
        assert confirm == 'THANK YOU FOR YOUR ORDER'

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_menu).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_logout).click()

        assert self.driver.current_url == 'https://www.saucedemo.com/v1/index.html'