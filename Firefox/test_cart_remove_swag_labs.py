from requests.auth import HTTPBasicAuth
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from Firefox.login_data import LoginData
from Firefox.login_data import ElemLocators
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



        item_count = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_cart_badge).text
        assert item_count == '2'
        print("SUCCESS # PRODUCT ADDED SUCCESSFULLY")