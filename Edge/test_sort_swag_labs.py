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
    
    def test_sorted_za_standard_user(self, launch_driver):
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

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_productsort).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_za).click()
        
        items_after_sorting = [element.text for element in self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")]
        assert items_after_sorting == sorted(items_after_sorting, reverse=sorted)



    def test_sorted_az_standard_user(self, launch_driver):
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

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_productsort).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_za).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_productsort).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_az).click()
        
        items_after_sorting = [element.text for element in self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")]
        assert items_after_sorting == (items_after_sorting)


    def test_sorted_lohi_standard_user(self, launch_driver):
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

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_productsort).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_lohi).click()

        prices_after_sorting = [float(element.text.replace('$', '')) for element in self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")]
        assert prices_after_sorting == sorted(prices_after_sorting)


    def test_sorted_hilo_standard_user(self, launch_driver):
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

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_productsort).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_hilo).click()

        prices_after_sorting = [float(element.text.replace('$', '')) for element in self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")]
        assert prices_after_sorting == sorted(prices_after_sorting, reverse=sorted)


    def test_sorted_za_problem_user(self, launch_driver):
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

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_productsort).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_za).click()

        items_after_sorting = [element.text for element in self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")]
        assert items_after_sorting == sorted(items_after_sorting, reverse=sorted)



    def test_sorted_az_problem_user(self, launch_driver):
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

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_productsort).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_za).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_productsort).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_az).click()
        
        items_after_sorting = [element.text for element in self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")]
        assert items_after_sorting == (items_after_sorting)


    def test_sorted_lohi_problem_user(self, launch_driver):
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

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_productsort).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_lohi).click()

        prices_after_sorting = [float(element.text.replace('$', '')) for element in self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")]
        assert prices_after_sorting == sorted(prices_after_sorting)


    def test_sorted_hilo_problem_user(self, launch_driver):
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

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_productsort).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_hilo).click()

        prices_after_sorting = [float(element.text.replace('$', '')) for element in self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")]
        assert prices_after_sorting == sorted(prices_after_sorting, reverse=sorted)


    def test_sorted_za_glitch_user(self, launch_driver):
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

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_productsort).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_za).click()
        
        items_after_sorting = [element.text for element in self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")]
        assert items_after_sorting == sorted(items_after_sorting, reverse=sorted)



    def test_sorted_az_glitch_user(self, launch_driver):
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

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_productsort).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_za).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_productsort).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_az).click()
        
        items_after_sorting = [element.text for element in self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")]
        assert items_after_sorting == (items_after_sorting)


    def test_sorted_lohi_glitch_user(self, launch_driver):
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

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_productsort).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_lohi).click()

        prices_after_sorting = [float(element.text.replace('$', '')) for element in self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")]
        assert prices_after_sorting == sorted(prices_after_sorting)


    def test_sorted_hilo_glitch_user(self, launch_driver):
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

        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_productsort).click()
        self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_hilo).click()

        prices_after_sorting = [float(element.text.replace('$', '')) for element in self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")]
        assert prices_after_sorting == sorted(prices_after_sorting, reverse=sorted)