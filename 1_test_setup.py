import time
from selenium import webdriver

print("Booting up the engine...")

# This physically launches your Chrome browser
driver = webdriver.Chrome()

print("Navigating to Shopify...")
# This commands the browser to go to a URL
driver.get("https://www.shopify.com")

# Pause for 5 seconds so you can see it working
time.sleep(5)

print("Shutting down...")
# This kills the browser window
driver.quit()