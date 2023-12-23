class LoginData:
    user1 = "standard_user"
    user2 = "locked_out_user"
    user3 = "problem_user"
    user4 = "performance_glitch_user"
    password = "secret_sauce"
    wrong_password = "pass123"


class CartData:
    firstname = "Rickard"
    lastname = "Pegado"
    zipcode = "61238"
    product_rate1 = 29.99
    product_rate2 = 9.99
    tax1 = 3.20


class ElemLocators:
    xpath_username = '//input[@id="user-name"]'
    xpath_password = '//input[@id="password"]'
    xpath_login = '//input[@id="login-button"]'
    xpath_product = "/html/body/div/div[2]/div[2]/div/div[1]/div[3]/div"
    xpath_lockeduser = '/html/body/div[2]/div[1]/div/div/form/h3'
    xpath_invalid_login = "/html/body/div[2]/div[1]/div/div/form/h3"
    xpath_menu = "/html/body/div/div[1]/div/div[3]/div"
    xpath_logout = '//a[@id="logout_sidebar_link"]'
    xpath_backpack = '//*[@id="inventory_container"]/div/div[1]/div[3]/button'
    xpath_jacket = '//*[@id="inventory_container"]/div/div[4]/div[3]/button'
    xpath_boltshirt = '//*[@id="inventory_container"]/div/div[3]/div[3]/button'
    xpath_bike = '//*[@id="inventory_container"]/div/div[2]/div[3]/button'
    xpath_onesie = '//*[@id="inventory_container"]/div/div[5]/div[3]/button'
    xpath_redshirt = '//*[@id="inventory_container"]/div/div[6]/div[3]/button'
    xpath_cart_badge = '//div[@id="shopping_cart_container"]/a/span'
    xpath_cart = '//div[@id="shopping_cart_container"]/a'
    xpath_cart1 = '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/button'
    xpath_cart2 = '//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[2]/button'
    xpath_cart3 = '//*[@id="cart_contents_container"]/div/div[1]/div[5]/div[2]/div[2]/button'
    xpath_cart4 = '//*[@id="cart_contents_container"]/div/div[1]/div[6]/div[2]/div[2]/button'
    xpath_cart5 = '//*[@id="cart_contents_container"]/div/div[1]/div[7]/div[2]/div[2]/button'
    xpath_cart6 = '//*[@id="cart_contents_container"]/div/div[1]/div[8]/div[2]/div[2]/button'
    xpath_continueshopping = '/html/body/div/div[2]/div[3]/div/div[2]/a[1]'
    xpath_checkout = '/html/body/div/div[2]/div[3]/div/div[2]/a[2]'
    xpath_firstname = '//input[@id="first-name"]'
    xpath_lastname = '//input[@id="last-name"]'
    xpath_zipcode = '//input[@id="postal-code"]'
    xpath_continue = '//*[@id="checkout_info_container"]/div/form/div[2]/input'
    xpath_total = '//div[@id="checkout_summary_container"]/div/div[2]/div[7]'
    xpath_finish = '/html/body/div/div[2]/div[3]/div/div[2]/div[8]/a[2]'
    xpath_confirm = '/html/body/div/div[2]/div[3]/h2'
    xpath_productsort = "/html/body/div/div[2]/div[2]/div/div[1]/div[3]/select"
    xpath_az = "/html/body/div/div[2]/div[2]/div/div[1]/div[3]/select/option[1]"
    xpath_za = "/html/body/div/div[2]/div[2]/div/div[1]/div[3]/select/option[2]"
    xpath_lohi = "/html/body/div/div[2]/div[2]/div/div[1]/div[3]/select/option[3]"
    xpath_hilo = "/html/body/div/div[2]/div[2]/div/div[1]/div[3]/select/option[4]"
    xpath_inventoryitem = '//*[@id="inventory_container"]'
    xpath_cartitem = '//*[@id="cart_contents_container"]'
    xpath_backpackpage = '/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/a/div'
    xpath_bikepage = '/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/a/div'
    xpath_boltpage = '/html/body/div/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/a/div'
    xpath_fleecepage = '/html/body/div/div[2]/div[2]/div/div[2]/div/div[4]/div[2]/a/div'
    xpath_onesiepage = '/html/body/div/div[2]/div[2]/div/div[2]/div/div[5]/div[2]/a/div'
    xpath_tshirtpage = '/html/body/div/div[2]/div[2]/div/div[2]/div/div[6]/div[2]/a/div'
    xpath_backbutton = '/html/body/div/div[2]/div[2]/div/button'

items_desc_list = [ElemLocators.xpath_backpackpage, ElemLocators.xpath_bikepage,
              ElemLocators.xpath_boltpage, ElemLocators.xpath_fleecepage,
              ElemLocators.xpath_onesiepage, ElemLocators.xpath_tshirtpage]

items_list = [ElemLocators.xpath_backpack, ElemLocators.xpath_bike,
                  ElemLocators.xpath_boltshirt, ElemLocators.xpath_jacket,
                  ElemLocators.xpath_onesie, ElemLocators.xpath_redshirt]   

cart_button_list = [ElemLocators.xpath_cart1, ElemLocators.xpath_cart2, 
                    ElemLocators.xpath_cart3, ElemLocators.xpath_cart4, 
                    ElemLocators.xpath_cart5, ElemLocators.xpath_cart6]




        # item_count = self.driver.find_element(by=By.XPATH, value=ElemLocators.xpath_cart_badge).text
        # assert item_count == str(len(items_buy_list))
        # print("SUCCESS # PRODUCT ADDED SUCCESSFULLY")