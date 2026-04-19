# from shopify_page import CartPage

# my_chrome = 'Chrome100' 

# def test_disc():
#     disc1 = cart_page(my_chrome)
#     act_result = disc1.apply_discount("FREESHIP")
#     exp_result = "Promo apllied successfully"
#     assert act_result == exp_result , "Test Failed : Discount code did not apply successfully"


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shopify_page import CartPage  # Make sure this matches your class name exactly



# THE DATA ENGINE: A list of tuples containing (promo_code, expected_result)
@pytest.mark.parametrize("promo, expected", [
    ("FREESHIP", "Promo apllied successfully"),
    ("SAVE20", "Promo apllied successfully"),
    ("JUNKCODE", "error")
])
def test_disc(promo, expected):

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    my_chrome = webdriver.Chrome(options=chrome_options)
    # 1. Build the object
    disc1 = CartPage(my_chrome)
    
    # 2. Command the object (Injecting the variable 'promo' instead of a hardcoded string)
    act_result = disc1.apply_discount(promo)
    
    # 3. The Judge (Asserting against the variable 'expected')
    assert act_result == expected, f"Test Failed: Code {promo} did not return {expected}"

    my_chrome.quit()