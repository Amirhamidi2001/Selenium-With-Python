import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True}
    )
driver.get("https://github.com")

print(driver.title)
assert "GitHub" in driver.title

elem = driver.find_element(By.NAME, "q")
elem.send_keys("dzitkowskik")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

driver.close()
