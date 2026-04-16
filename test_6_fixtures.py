import pytest
from selenium import webdriver

# 1. THE MANAGER (The Fixture)
# The @pytest.fixture tag tells PyTest this is a setup/teardown engine, not a test.
@pytest.fixture
def browser_engine():
    print("\n[SETUP] Booting up physical Chrome...")
    driver = webdriver.Chrome()
    
    # YIELD pauses the fixture and passes the live driver to the test below.
    yield driver 
    
    # TEARDOWN: This runs the exact millisecond the test finishes.
    print("\n[TEARDOWN] Test complete. Force-closing Chrome to clear RAM.")
    driver.quit()

# 2. THE TEST
# Notice we pass the exact name of the fixture into the test parameters.
def test_saucedemo_page_load(browser_engine):
    # The fixture hands us the live driver
    driver = browser_engine 
    
    print("[TEST] Navigating to website...")
    driver.get("https://www.saucedemo.com/")
    
    # We grab the actual title from the HTML tab
    actual_title = driver.title
    expected_title = "Swag Labs"
    
    print(f"[TEST] Verifying title is '{expected_title}'...")
    assert actual_title == expected_title, f"Bug: Expected {expected_title} but got {actual_title}"