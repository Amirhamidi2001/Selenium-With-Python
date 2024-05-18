from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

hub_url = "http://172.17.0.1:4444/wd/hub"

driver = webdriver.Remote(
			command_executor = 'http://127.0.0.1:4444/wd/hub',
			desired_capabilities = {
			'browserName': 'firefox',
			'javascriptEnabled': True
			})

driver.get("http://www.python.org")
driver.close()
