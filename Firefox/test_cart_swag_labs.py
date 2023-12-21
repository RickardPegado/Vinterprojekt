from requests.auth import HTTPBasicAuth
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from login_users import LoginData
from login_users import ElemLocators
from time import sleep as wait
import time
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

    def test_addtocart_standard(self, launch_driver):
        self.driver.get(self.url)
        assert self.driver.current_url == "https://www.saucedemo.com/v1/index.html"
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).send_keys(LoginData.user1)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).get_attribute('value') == LoginData.user1
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).send_keys(LoginData.password)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).get_attribute('value') == LoginData.password
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_login).click()
        product = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_product).text
        assert product == 'Products'
        
        try:
            absent_element = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_cart_badge)
        except NoSuchElementException:
        
            assert True
        else:
        
            assert False            

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_backpack).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_jacket).click()

        item_count = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_cart_badge).text
        assert item_count == '2'
        print("SUCCESS # PRODUCT ADDED SUCCESSFULLY")

    
    def test_addtocart_problem(self, launch_driver):
        self.driver.get(self.url)
        assert self.driver.current_url == "https://www.saucedemo.com/v1/index.html"
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).send_keys(LoginData.user3)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).get_attribute('value') == LoginData.user3
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).send_keys(LoginData.password)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).get_attribute('value') == LoginData.password
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_login).click()
        product = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_product).text
        assert product == 'Products'
        
        try:
            absent_element = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_cart_badge)
        except NoSuchElementException:
        
            assert True
        else:
        
            assert False            

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_bike).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_boltshirt).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_redshirt).click()

        item_count = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_cart_badge).text
        assert item_count == '3'
        print("SUCCESS # PRODUCT ADDED SUCCESSFULLY")


    def test_addtocart_glitch(self, launch_driver):
        self.driver.get(self.url)
        assert self.driver.current_url == "https://www.saucedemo.com/v1/index.html"
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).send_keys(LoginData.user3)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).get_attribute('value') == LoginData.user3
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).send_keys(LoginData.password)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).get_attribute('value') == LoginData.password
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_login).click()
        product = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_product).text
        assert product == 'Products'
        
        try:
            absent_element = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_cart_badge)
        except NoSuchElementException:
        
            assert True
        else:
        
            assert False            

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_bike).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_boltshirt).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_redshirt).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_backpack).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_jacket).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_onesie).click()

        item_count = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_cart_badge).text
        assert item_count == '6'
        print("SUCCESS # PRODUCT ADDED SUCCESSFULLY")