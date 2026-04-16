import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. THE BLUEPRINT (Page Object Model)
class LoginPage:
    
    def __init__(self, driver):
        # Packing the browser into the backpack
        self.browser = driver
        
        # Storing the exact HTML IDs found on saucedemo.com
        self.username_box = "user-name"
        self.password_box = "password"
        self.login_btn = "login-button"

    def execute_login(self, username, password):
        print(f"Injecting credentials for: {username}")
        
        # The browser uses the map to find the boxes and physically type
        self.browser.find_element(By.ID, self.username_box).send_keys(username)
        self.browser.find_element(By.ID, self.password_box).send_keys(password)
        
        # The browser finds the button and physically clicks it
        self.browser.find_element(By.ID, self.login_btn).click()


# 2. THE EXECUTION ZONE
print("Booting up Selenium...")
my_chrome = webdriver.Chrome()

print("Navigating to e-commerce site...")
my_chrome.get("https://www.saucedemo.com/")
time.sleep(2) # Pausing for 2 seconds to let the page render

# Building the Object from the Blueprint
login_page = LoginPage(my_chrome)

# Commanding the Object using the site's official test credentials
login_page.execute_login("standard_user", "secret_sauce")

print("Login successful. Holding for 5 seconds...")
time.sleep(5)

print("Shutting down engine.")
my_chrome.quit()