from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Configure the remote WebDriver using Selenium Grid
capabilities = DesiredCapabilities.FIREFOX.copy()
capabilities['browserName'] = 'firefox'

# Replace 'localhost:4444' with the actual address of your Selenium Grid hub
grid_url = 'http://localhost:4444/wd/hub'

# Create a remote WebDriver instance pointing to the Selenium Grid hub
driver = webdriver.Remote(command_executor=grid_url, desired_capabilities=capabilities)

# Open the Python website
driver.get('http://www.python.org')

# Perform any further actions as needed...

# Close the browser
# driver.quit()
