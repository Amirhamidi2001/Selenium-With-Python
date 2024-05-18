from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from time import sleep

# hub_url = "http://127.0.0.1:4444/wd/hub"
hub_url = "http://172.17.0.1:4444/wd/hub"

options = Options()
options.add_argument("--start-maximized")
desired_capabilities = DesiredCapabilities.CHROME.copy()
# desired_capabilities.update(options.to_capabilities())

try:
    driver = webdriver.Remote(command_executor=hub_url, options=options, desired_capabilities=desired_capabilities)
except Exception as e:
    print("Error submitting form: ", e)

driver.get("http://www.python.org")
print("The test was done successfully")
sleep(5)
driver.quit()
