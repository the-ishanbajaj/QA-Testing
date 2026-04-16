from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

class invent :
    def __init__(self,browser_engine) :
        self.browser= browser_engine

        self.search_bar = "product_search_id"

    def search_product(self , product) :

        self.browser.find_element(By.ID , self.search_bar).send_keys(product)


my_chrome= webdriver.Chrome()

pro1 = invent(my_chrome)

pro1.search_product("ishan")