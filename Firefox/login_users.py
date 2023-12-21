class LoginData:
    user1 = "standard_user"
    user2 = "locked_out_user"
    user3 = "problem_user"
    user4 = "performance_glitch_user"
    password = "secret_sauce"
    wrong_password = "pass123"


class ElemLocators:
    xpath_username = '//input[@id="user-name"]'
    xpath_password = '//input[@id="password"]'
    xpath_login = '//input[@id="login-button"]'
    xpath_product = "/html/body/div/div[2]/div[2]/div/div[1]/div[3]/div"
    xpath_lockeduser = '/html/body/div[2]/div[1]/div/div/form/h3'
    xpath_invalid_login = "/html/body/div[2]/div[1]/div/div/form/h3"
    xpath_menu = '//button[@id="react-burger-menu-btn"]'
    xpath_logout = '//a[@id="logout_sidebar_link"]'
    xpath_backpack = '/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/button'
    xpath_jacket = '/html/body/div/div[2]/div[2]/div/div[2]/div/div[4]/div[3]/button'
    xpath_boltshirt = "/html/body/div/div[2]/div[2]/div/div[2]/div/div[3]/div[3]/button"
    xpath_bike = "/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/button"
    xpath_onesie = "/html/body/div/div[2]/div[2]/div/div[2]/div/div[5]/div[3]/button"
    xpath_redshirt = "/html/body/div/div[2]/div[2]/div/div[2]/div/div[6]/div[3]/button"
    xpath_cart_badge = '//div[@id="shopping_cart_container"]/a/span'
    xpath_cart = '//div[@id="shopping_cart_container"]/a'
    xpath_checkout = '//button[@id="checkout"]'
    xpath_firstname = '//input[@id="first-name"]'
    xpath_lastname = '//input[@id="last-name"]'
    xpath_zipcode = '//input[@id="postal-code"]'
    xpath_continue = '//input[@id="continue"]'
    xpath_total = '//div[@id="checkout_summary_container"]/div/div[2]/div[8]'