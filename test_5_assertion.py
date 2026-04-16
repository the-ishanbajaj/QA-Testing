from selenium import webdriver
from selenium.webdriver.common.by import By

class inventory :
    def __init__(self,browser_engine) :
        self.browser = browser_engine 
        self.search_bar = "product_name"

    def product_search(self , p_name) :
        print(f"typing {p_name} in {self.search_bar}")
        if p_name == "milk" :
            return "https://dairy-admin.com/search?q=milk"
        else :
            return  "https://dairy-admin.com/search-failed"
        
def test_product_search() :
    my_chrome = webdriver.Chrome()
    pro1 = inventory(my_chrome)
    result = pro1.product_search("milk")
    assert result == "https://dairy-admin.com/search?q=milk" , "Test Failed : Search for milk did not return expected URL"
    print("Test Passed : Search for milk returned expected URL")
    my_chrome.quit()
