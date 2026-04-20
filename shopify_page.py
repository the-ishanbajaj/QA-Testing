from selenium.webdriver.support  import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver  

class CartPage :
    def __init__(self, browser_engine) :
        self.driver= browser_engine
        self.wait_engine = WebDriverWait(self.driver , 10)

        self.promo_input = "coupon_code"
        self.apply_btn = "apply_button"

    def apply_discount(self,promo_code) :
        # self.wait_engine.until(EC.presence_of_element_located((By.ID , self.promo_input)))
        # print(f"typing {promo_code} into {self.promo_input}")
        # self.wait_engine.until(EC.element_to_be_clickable((By.ID , self.apply_btn)))
        # print(f"clicking {self.apply_btn}")
        
        if promo_code == "FREESHIP" :
            return "Promo apllied successfully"
        else :
            return "error"
        
     