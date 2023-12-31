from selenium import webdriver
from selenium.webdriver.common.by import By
from login_data import LoginData
from login_data import ElemLocators
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
    
    def test_T1_login_standard_user(self, launch_driver):
        self.driver.get(self.url)
        assert self.driver.current_url == "https://www.saucedemo.com/v1/index.html"
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).send_keys(LoginData.user1)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).get_attribute('value') == LoginData.user1
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).send_keys(LoginData.password)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).get_attribute('value') == LoginData.password
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_login).click()
        product = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_product).text
        assert product == 'Products'
        print("SUCCESS # LOGGED IN WITH USERNAME {username} and PASSWORD {password}".format(username=LoginData.user1, password=LoginData.password))

    
    def test_T2_login_locked_user(self, launch_driver):
        self.driver.get(self.url)
        assert self.driver.current_url == "https://www.saucedemo.com/v1/index.html"
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).send_keys(LoginData.user2)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).get_attribute('value') == LoginData.user2
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).send_keys(LoginData.password)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).get_attribute('value') == LoginData.password
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_login).click()
        lock = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_lockeduser).text
        assert lock == 'Epic sadface: Sorry, this user has been locked out.'
        print("SUCCESS # USER LOCKED OUT")

    
    def test_T3_login_problem_user(self, launch_driver):
        self.driver.get(self.url)
        assert self.driver.current_url == "https://www.saucedemo.com/v1/index.html"
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).send_keys(LoginData.user3)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).get_attribute('value') == LoginData.user3
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).send_keys(LoginData.password)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).get_attribute('value') == LoginData.password
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_login).click()
        product = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_product).text
        assert product == 'Products'
        print("SUCCESS # LOGGED IN WITH USERNAME {username} and PASSWORD {password}".format(username=LoginData.user3, password=LoginData.password))
    
    
    def test_T4_login_glitch_user(self, launch_driver):
        self.driver.get(self.url)
        assert self.driver.current_url == "https://www.saucedemo.com/v1/index.html"
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).send_keys(LoginData.user4)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).get_attribute('value') == LoginData.user4
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).send_keys(LoginData.password)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).get_attribute('value') == LoginData.password
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_login).click()
        product = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_product).text
        assert product == 'Products'
        print("SUCCESS # LOGGED IN WITH USERNAME {username} and PASSWORD {password}".format(username=LoginData.user4, password=LoginData.password))


    def test_T5_invalid_password(self, launch_driver):
        self.driver.get(self.url)
        assert self.driver.current_url == "https://www.saucedemo.com/v1/index.html"
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).send_keys(LoginData.user1)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_username).get_attribute('value') == LoginData.user1
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).send_keys(LoginData.wrong_password)
        assert self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_password).get_attribute('value') == LoginData.wrong_password
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_login).click()
        invalid = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_invalid_login).text
        assert invalid == 'Epic sadface: Username and password do not match any user in this service'
        print("SUCCESS # INVALID LOGIN WITH USERNAME {username} and PASSWORD {password}".format(username=LoginData.user1, password=LoginData.wrong_password))