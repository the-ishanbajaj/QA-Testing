
class cart_page :
    def __init__(self, browser_engine) :
        self.driver= browser_engine

        self.promo_input = "coupon_code"
        self.apply_btn = "apply_button"

    def apply_discount(self,promo_code) :
        print(f"typing {promo_code} into {self.promo_input}")
        print(f"clicking {self.apply_btn}")
        
        if promo_code == "FREESHIP" :
            return "Promo apllied successfully"
        else :
            return "error"
        
    