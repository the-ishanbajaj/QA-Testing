from shopify_page import cart_page

my_chrome = 'Chrome100' 

def test_disc():
    disc1 = cart_page(my_chrome)
    act_result = disc1.apply_discount("FREESHIP")
    exp_result = "Promo apllied successfully"
    assert act_result == exp_result , "Test Failed : Discount code did not apply successfully"