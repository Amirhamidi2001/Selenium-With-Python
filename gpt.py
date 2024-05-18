from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Define the desired capabilities for the remote browser
capabilities = DesiredCapabilities.FIREFOX.copy()
capabilities['platform'] = 'ANY'
capabilities['browserName'] = 'firefox'

# Specify the URL of the Selenium Grid hub
grid_url = 'http://127.0.0.1:4444/wd/hub'  # Replace with your Selenium Grid hub URL

# Create a remote webdriver instance
driver = webdriver.Remote(command_executor=grid_url, desired_capabilities=capabilities)

# Open the desired URL
driver.get("http://www.python.org")

# Perform actions on the webpage as needed
# ...

# Close the browser
driver.quit()
